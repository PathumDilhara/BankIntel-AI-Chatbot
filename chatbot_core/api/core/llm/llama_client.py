from langchain_ollama import ChatOllama

class LlamaClient:

    def __init__(self):
        # Loads the LLaMA model once when the class is created otherwise we have to generate model dor weach request
        self.llm = ChatOllama(
            model = "llama3",
            temperature=0.7,
        )

    # Send the prompt to the model and get response as str
    def generate(self, prompt:str)-> str:
        response = self.llm.invoke(prompt)
        return response.content # str