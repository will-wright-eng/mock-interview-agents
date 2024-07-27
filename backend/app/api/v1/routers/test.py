import os

from fastapi import APIRouter

from app.core.config import settings

PORT = os.environ.get("TRACKING_BACKEND_PORT")
router = r = APIRouter(
    prefix="/test",
)


@r.get("/test")
def test():
    return {"Hello": str(os.listdir())}


@r.get("/project")
def project():
    return {"Hello": settings.PROJECT_NAME}


@r.get("/port")
def project():
    return {"Hello": str(PORT)}
