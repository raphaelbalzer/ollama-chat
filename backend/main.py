from fastapi import FastAPI
from chat_request import ChatRequest
from ollama_client import OllamaClient
#from sse_starlette import EventSourceResponse

app = FastAPI()

@app.post('/chat')
def chat_endpoint(req: ChatRequest):
    ollama_client = OllamaClient(model=req.model)
    answer = "".join(chunk for chunk in ollama_client.generate(prompt=req.message))
    return {"response": answer}

# @app.post("/sse")
# async def chat_stream(req: ChatRequest):
#     client = OllamaClient(model=req.model)

#     async def event_generator():
#         for chunk in client.generate(req.message):
#             yield {"event": "message", "data": chunk}

#     return EventSourceResponse(event_generator())