from groq import Groq
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings
from app.prompts.prompts import *

router = r = APIRouter(
    prefix="/doc_gen",
)

MODEL = "llama3.1-70b-versatile"


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
        model=MODEL,
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
        model=MODEL,
    )
    questions = [choice.message.content for choice in questions_completion.choices]
    return {"questions": questions}

class ReportCardRequest(BaseModel):
    question_bank: str
    transcript: str
    overall_rubric: str

@r.post("/generate_report_card")
async def generate_report_card(request: ReportCardRequest):
    
    client = Groq(
        api_key=settings.GROQ_API_KEY,
    )

    content = f"Transcript: {request.transcript}\n\nQuestion Bank: {request.question_bank}\n\nOverall Rubric: {request.overall_rubric}"

    report_card_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": report_card_prompt["system"],
            },
            {
                "role": "user",
                "content": content,
            },
        ],
        model=MODEL,
    )
    report_card = report_card_completion.choices[0].message.content
    return {"report_card": report_card}