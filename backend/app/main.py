import os

from fastapi import FastAPI, Request
from vapi_python import Vapi
from groq import Groq
# from fastapi.middleware.cors import CORSMiddleware

from app.core.log import logger
from app.core.config import settings
from app.api.v1.routers import test, vapi, doc_gen

app = FastAPI(title=settings.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")

PORT = os.environ.get("TRACKING_BACKEND_PORT")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")
    app.state.vapi = Vapi(api_key=settings.VAPI_API_KEY)
    app.state.groq = Groq(
        api_key=settings.GROQ_API_KEY,
    )


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/info")
async def info():
    return settings.model_dump()


# Routers
app.include_router(
    test.router,
    prefix="/api/v1",
    tags=["test"],
)
app.include_router(
    doc_gen.router,
    prefix="/api/v1",
    tags=["doc_gen"],
)

app.include_router(
    vapi.router,
    prefix="/api/v1",
    tags=["vapi"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods
#     allow_headers=["*"],  # Allow all headers
# )