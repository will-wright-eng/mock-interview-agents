import os


class Settings:
    PROJECT_NAME: str = "mock-interview-agents"
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY")

settings = Settings()
