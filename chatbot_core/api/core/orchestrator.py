from core.llm.llama_client import LlamaClient
from core.llm.prompt_builder import PromptBuilder

class ChatOrchestrator:

    def __init__(self):
        self.llama = LlamaClient()
        self.prompt = PromptBuilder()
    
    def get_response(self, user_message:str)-> str:

        # 1. Classify intent with BERT

        
        # 2. Retrieve relevant context from vector DB

        
        # 3. Build the prompt
        prompt = self.prompt.build_prompt(user_message=user_message)

        # 4. Generate answer with LLaMA
        response = self.llama.generate(prompt=prompt)
        
        # 5. Return final response
        return response