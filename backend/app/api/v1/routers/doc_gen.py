from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.config import settings
from app.core.log import logger
from app.prompts.doc_gen import rubric_gen_prompt, question_gen_prompt, cv_gen_prompt

router = r = APIRouter(
    prefix="/doc_gen",
)


class ChatRequest(BaseModel):
    content: str


class ChatResponse(BaseModel):
    response: str


@r.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    client = request.app.state.groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request.content,
            },
        ],
        model=settings.GROQ_MODEL,
    )
    return ChatResponse(response=chat_completion.choices[0].message.content)


class DocGenRequest(BaseModel):
    type: str = "questions"

@r.post("/generate_questions_and_rubric")
async def generate_questions_and_rubric(request: Request):
    client = request.app.state.groq
    data = await request.json()
    # Extract job_title and cv from the data
    job_title = data.get("job_title")
    cv = data.get("cv")

    formatted_request_content = f"Job title: {job_title}\n\n{question_gen_prompt}\n\nCV:\n{cv}"
    logger.info(f"Formatted request content: {formatted_request_content}")

    questions_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_request_content,
            },
        ],
        model=settings.GROQ_MODEL,
    )
    questions = questions_completion.choices[0].message.content
    return {"questions": questions}


@r.post("/generate_cv")
async def generate_cv(request: Request, job_title: str):
    client = request.app.state.groq
    request_content = cv_gen_prompt.format(JOB_TITLE=job_title)
    logger.info(f"Request content: {request_content}")

    questions_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request_content,
            },
        ],
        model=settings.GROQ_MODEL,
    )
    return {"cv": questions_completion.choices[0].message.content}