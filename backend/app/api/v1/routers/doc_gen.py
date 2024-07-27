from groq import Groq
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings
from backend.app.prompts.prompts import rubric_gen_prompt, question_gen_prompt

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


class DocGenRequest(BaseModel):
    type: str = "questions"


@r.post("/generate_questions")
async def generate_doc(request: DocGenRequest):
    if request.type == "questions":
        request_content = question_gen_prompt
    elif request.type == "rubric":
        request_content = rubric_gen_prompt
    else:
        raise ValueError(f"Invalid type: {request.type}")

    client = Groq(
        api_key=settings.GROQ_API_KEY,
    )
    questions_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request_content,
            },
        ],
        model="llama3-8b-8192",
    )
    questions = [choice.message.content for choice in questions_completion.choices]
    return {"questions": questions}
