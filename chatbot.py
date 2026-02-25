from openai import OpenAI

class OpenAIConfig:
    def __init__(self, api_key: str = "api", model: str = "gpt-4o-mini"):
        """
        Initializes the OpenAI API configuration with the given API key and model.
        """
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.conversation_history = [
            {"role": "system", "content": "You are a helpful information assistant. Provide concise and accurate information."}
        ]

    def get_response(self, prompt: str, history: list) -> str:
        """
        Sends a prompt to the OpenAI API and returns the response text.
        Maintains conversation history for context.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=history + [{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content
        return reply