class PromptBuilder:
    
    def build_prompt(self, user_message:str)-> str:
        prompt = f"""
                You are a helpful banking assistant chatbot.

                Answer the user clearly and professionally.

                User question:
                {user_message}
        """

        return prompt.strip()