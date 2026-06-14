from core.llm.llama_client import LlamaClient
from core.llm.prompt_builder import PromptBuilder
from core.rag.retriever import Retriever
from core.memory.chat_history import ChatMemory
from core.bert.intent_classifier import BERTIntentClassifer

class ChatOrchestrator:

    def __init__(self):
        self.llama = LlamaClient()
        self.prompt = PromptBuilder()
        self.retriever = Retriever()
        self.chat_memory = ChatMemory()
        self.bert_classifier= BERTIntentClassifer()
 
    def get_response(self, user_message:str)-> str:
       
        print(f"### User message : {user_message}")

        # 1. ====================== Retrieve relevant context from vector DB ======================
        # if histrory is not empty
        if self.chat_memory.history:

            # build the user message updating prompt according to the chat history
            msg_update_prompt= self.prompt.build_question_update_prompt(
                user_message=user_message, 
                chat_history=self.chat_memory.history
                )
            updated_message= self.llama.generate(prompt=msg_update_prompt)
            
        else:
            updated_message=user_message

        print(f"### Updated message : {updated_message}")
        relevant_docs = self.retriever.get_relevant_docs(query= updated_message)

        # Convert docs_list → text
        combined_docs = "\n".join([f" - {doc.page_content}" for doc in relevant_docs])
        #print("### 2 ", combined_docs)

        # 2. ====================== Classify intent with BERT ======================
        intent = "unknwon"

        i, c = self.bert_classifier.predict(msg=updated_message).values()
        
        if c >= 0.5:
            intent=i

        # 3. ====================== Build the final answer prompt ======================
        prompt = self.prompt.build_prompt(
            user_message=updated_message, 
            intent=intent, 
            context =combined_docs, 
            chat_history=self.chat_memory.history
            )
        #print("### 3 ", prompt)

        # 4. ====================== Generate answer with LLaMA ======================
        response = self.llama.generate(prompt=prompt)
        print("### 4 ", response)

        # 5. ====================== update chat history ======================
        self.chat_memory.add(user_message=updated_message, bot_response=response)
        
        # 6. ====================== Return final response ======================
        return {
            "intent": intent,
            "response": response
        } # dic