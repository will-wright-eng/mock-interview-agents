import os
from fastapi import FastAPI, Request

from .core.config import settings
from .core.log import logger
from .api.v1.routers.test import router
from .api.v1.routers.doc_gen import router


app = FastAPI(title=settings.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")

PORT = os.environ.get("TRACKING_BACKEND_PORT")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/info")
async def info():
    return settings.model_dump()

# Routers
app.include_router(
    router,
    prefix="/api/v1",
    tags=["test"]
)
app.include_router(
    router,
    prefix="/api/v1",
    tags=["doc_gen"]
)

