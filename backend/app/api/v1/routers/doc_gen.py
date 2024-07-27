from fastapi import HTTPException
from pydantic import BaseModel
import httpx

from fastapi import APIRouter

from app.core.config import settings

router = r = APIRouter(
    prefix="/doc_gen",
)


class ConversationInput(BaseModel):
    prompt: str

class ConversationResponse(BaseModel):
    response: str

async def call_groq_api(prompt: str) -> str:
    # Replace with the actual Groq API endpoint and any required headers/authentication
    groq_api_url = "https://api.groq.com/v1/endpoint"
    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"prompt": prompt}

    async with httpx.AsyncClient() as client:
        response = await client.post(groq_api_url, json=payload, headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error calling Groq API")

        return response.json().get("response")

@r.post("/converse", response_model=ConversationResponse)
async def converse(input: ConversationInput):
    try:
        response_text = await call_groq_api(input.prompt)
        return ConversationResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
