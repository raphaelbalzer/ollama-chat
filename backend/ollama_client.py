from ollama import chat

class OllamaClient():
    def __init__(self, model:str):
        self.model = model

    def generate(self, prompt):
        stream = chat(
            model=self.model,
            messages=[{'role': 'user', 'content': f'{prompt}'}],
            stream=True
        )
        
        for chunk in stream:
            yield(chunk['message']['content'])
            