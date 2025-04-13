import requests

class OllamaGenerator:
    def __init__(self, model="llama3.2"):
        self.model = model
        self.api_url = "http://localhost:11434/api/generate"
        
    def generate_response(self, prompt, context=None):
        """Generate response using Ollama API"""
        system_prompt = """You are a helpful assistant. Provide concise and accurate answers to the 
        user's questions in around 20 words.Avoid adding
        formatting like asterisks or special characters unless explicitly requested."""
        
        context_str = ""
        if context:
            context_str = "\nPrevious conversation:\n" + "\n".join([
                f"User: {ex['user_message']}\nAssistant: {ex['bot_response']}"
                for ex in context[-3:]  # Include last 3 exchanges
            ])

        full_prompt = f"{system_prompt}\n{context_str}\nUser: {prompt}\nAssistant:"

        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    }
            )
            print(response.json()['response'])
            if response.status_code == 200:
                return response.json()['response']
            else:
                return "I apologize, but I'm having trouble generating a response right now."
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return "I apologize, but I'm having trouble connecting to the language model right now."

    def generate_wellness_suggestion(self, emotion, user_message):
        """Generate contextual wellness suggestion based on emotion"""
        prompt = f"""Given that the user is feeling {emotion}, and they said: "{user_message}"
        Provide a short, practical wellness suggestion that would be helpful in this situation.
        Keep the suggestion concise and actionable. Focus on immediate steps they can take.
        Avoid adding formatting like asterisks or special characters unless explicitly requested."""

        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                }
            )
            if response.status_code == 200:
                return response.json()['response']
            else:
                return "Remember to take care of yourself and practice self-care activities."
        except Exception as e:
            print(f"Error generating wellness suggestion: {str(e)}")
            return "Consider taking a moment for self-care and reflection."