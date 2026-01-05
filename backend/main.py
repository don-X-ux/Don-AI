from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "YOUR_API_KEY"

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": req.message}
        ]
    )
    return {
        "reply": response.choices[0].message.content
    }
