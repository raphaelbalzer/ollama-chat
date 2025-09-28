from fastapi import FastAPI
from chat_request import ChatRequest
from ollama_client import OllamaClient

app = FastAPI()

@app.post('/chat')
def chat_endpoint(req: ChatRequest):
    ollama_client = OllamaClient(model=req.model)
    ollama_client.generate(prompt=req.message)
