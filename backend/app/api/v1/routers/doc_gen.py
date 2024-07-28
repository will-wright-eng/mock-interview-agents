import json
from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.config import settings
from app.core.log import logger
from app.prompts.prompts import *


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
    job_title = data.get("jobTitle")
    job_description = data.get("jobDescription")
    company_name = data.get("company")
    logger.info(f"Job title: {job_title}, Company: {company_name}, Job Description: {job_description}")
    formatted_request_content = f"Job title: {job_title}\nCompany: {company_name}\n\n{job_description_prompt.get('system')}\n\nJob Description:\n{job_description}"
    logger.info(f"Formatted request content: {formatted_request_content}")

    questions_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": job_description_prompt.get("system"),
            },
            {
                "role": "user",
                "content": formatted_request_content,
            },
        ],
        model=settings.GROQ_MODEL,
        response_format={"type": "json_object"}
    )
    questions = questions_completion.choices[0].message.content
    logger.info(f"{questions}")
    questions_parsed = json.loads(questions)
    return questions_parsed


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
    

@r.post("/generate_report_card")
async def generate_report_card(request: Request):
    client = request.app.state.groq
    data = await request.json()
    transcript = data.get("transcript")
    question_bank = json.dumps(data.get("question_bank"))
    overall_rubric = json.dumps(data.get("overall_rubric"))
    company = data.get("company")
    job_title = data.get("job_title")
    job_description = data.get("job_description")
    content = f"Job Title: {job_title}\nCompany: {company}\n\nJob Description: {job_description}\n\nTranscript: {transcript}\n\nQuestion Bank: {question_bank}\n\nOverall Rubric: {overall_rubric}"
    logger.info(f"Content: {content}")
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
        model=settings.GROQ_MODEL,
        response_format={"type": "json_object"}
    )
    report_card = report_card_completion.choices[0].message.content
    logger.info(f"Report card: {report_card}")
    report_card_parsed = json.loads(report_card)
    return report_card_parsed

