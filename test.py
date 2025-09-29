import requests

res = requests.post(
    "http://127.0.0.1:8000/chat/stream",
    json={"model": "gemma3:4b", "message": "Hallo Ollama!"}
)
print(res.json())
