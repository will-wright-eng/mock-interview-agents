from groq import Groq
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings

router = r = APIRouter(
    prefix="/doc_gen",
)


class ChatRequest(BaseModel):
    content: str


class ChatResponse(BaseModel):
    response: str


@r.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    client = Groq(
        api_key=settings.GROQ_API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request.content,
            },
        ],
        model="llama3-8b-8192",
    )

    return ChatResponse(response=chat_completion.choices[0].message.content)
