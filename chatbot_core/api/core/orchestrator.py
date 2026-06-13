from core.llm.llama_client import LlamaClient
from core.llm.prompt_builder import PromptBuilder
from core.rag.retriever import Retriever

class ChatOrchestrator:

    def __init__(self):
        self.llama = LlamaClient()
        self.prompt = PromptBuilder()
        self.retriever = Retriever()
    
    def get_response(self, user_message:str)-> str:

        # 1. Classify intent with BERT
        intent = "unknwon"
        
        # 2. Retrieve relevant context from vector DB
        relevant_docs = self.retriever.get_relevant_docs(user_message)
        print("### 1 ", relevant_docs)
        
        # Convert docs_list → text
        combined_docs = "\n".join([f" - {doc.page_content}" for doc in relevant_docs])
        print("### 2 ", combined_docs)

        # 3. Build the prompt
        prompt = self.prompt.build_prompt(user_message=user_message, context =combined_docs, intent=intent)
        print("### 3 ", prompt)

        # 4. Generate answer with LLaMA
        response = self.llama.generate(prompt=prompt)
        print("### 4 ", response)

        # 5. Return final response
        return response