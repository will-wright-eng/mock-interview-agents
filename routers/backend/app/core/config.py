import os


class Settings:
    PROJECT_NAME: str = "mock-interview-agents"
    GROQ_API: str = os.environ.get("GROQ_API")

settings = Settings()
