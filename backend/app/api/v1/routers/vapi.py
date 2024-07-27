import os
import io
import sys
from fastapi import APIRouter
from vapi_python import Vapi
from app.core.config import settings

router = APIRouter(
    prefix="/vapi",
)

API_KEY = os.environ.get("VAPI_API_KEY", "ba5d2083-8501-4af5-8e57-7d48456ad979")
ASSISTANT_ID = os.environ.get("VAPI_ASSISTANT_ID", "d79b1e69-46bb-4ac3-983c-e3efd9a40269")

@router.post("/start")
def start_vapi():
    vapi = Vapi(api_key=API_KEY)
    
    # Redirect stdout to capture the output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    try:
        vapi.start(assistant_id=ASSISTANT_ID)
        output = buffer.getvalue()
        
        # Extract call_id from the output
        call_id = None
        for line in output.split('\n'):
            if line.startswith("Joining call..."):
                call_id = line.split()[-1]
                break
        
        return {
            "message": "Vapi started successfully",
            "call_id": call_id,
            "output": output
        }
    finally:
        # Restore stdout
        sys.stdout = old_stdout

@router.post("/stop")
def stop_vapi():
    vapi = Vapi(api_key=API_KEY)
    vapi.stop()
    return {"message": "Vapi stopped successfully"}

@router.get("/project")
def project():
    return {"project": settings.PROJECT_NAME}
