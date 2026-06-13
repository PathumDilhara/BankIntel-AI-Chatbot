class PromptBuilder:
    
    def build_prompt(self, user_message:str, context:str, intent:str)-> str:
        prompt = f"""
                You are a helpful banking assistant chatbot.

                Use the Context, Intent & user question below to answer the user.
                If Intent is unknown ignore it and moce with context.
                If context is empty, use general knowledge.

                Intent:
                {intent}

                --------------------
                Context:
                {context}
                --------------------

                User question:
                {user_message}

                Answer clearly and professionally.
                Don't include anything about soruces such as 'according to the information from documents'.
                Response should be less than 200 characters.
        """

        return prompt.strip() # str