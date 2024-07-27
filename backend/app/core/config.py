import os


class Settings:
    PROJECT_NAME: str = "mock-interview-agents"
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY", "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")
    VAPI_API_KEY: str = os.environ.get("VAPI_API_KEY", "ba5d2083-8501-4af5-8e57-7d48456ad979")
    VAPI_ASSISTANT_ID: str = os.environ.get("VAPI_ASSISTANT_ID", "d79b1e69-46bb-4ac3-983c-e3efd9a40269")
    GROQ_MODEL: str = "llama-3.1-8b-instant"
    # GROQ_MODEL: str = "llama-3.1-70b-versatile"


settings = Settings()
