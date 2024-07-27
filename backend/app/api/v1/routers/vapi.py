import io
import sys

from fastapi import Request, APIRouter

from app.core.config import settings

router = r = APIRouter(
    prefix="/vapi",
)

sample_assistant_overrides = {
    "variableValues": {
        "jobDescription": "This is a sample job description",
        "jobName": "Software Engineer",
        "companyName": "Groq",
        "questionBank": "Sample job bank"
    }
}

@r.post("/start")
async def start_vapi(request: Request):
    vapi = request.app.state.vapi

    # Get the assistant overrides from the request body
    # TODO: fix this later
    # assistant_overrides = await request.json()
    assistant_overrides = sample_assistant_overrides

    # Redirect stdout to capture the output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        vapi.start(assistant_id=settings.VAPI_ASSISTANT_ID, assistant_overrides=assistant_overrides)
        output = buffer.getvalue()

        # Extract call_id from the output
        call_id = None
        for line in output.split("\n"):
            if line.startswith("Joining call..."):
                call_id = line.split()[-1]
                break

        return {
            "message": "Vapi started successfully",
            "call_id": call_id,
            "output": output,
        }
    finally:
        # Restore stdout
        sys.stdout = old_stdout


@r.post("/stop")
def stop_vapi(request: Request):
    vapi = request.app.state.vapi
    vapi.stop()
    return {"message": "Vapi stopped successfully"}
