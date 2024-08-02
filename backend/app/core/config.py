import os


class Settings:
    PROJECT_NAME: str = "mock-interview-agents"
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY")
    # VAPI_API_KEY: str = os.environ.get("VAPI_API_KEY")
    VAPI_API_KEY_PUBLIC: str = os.environ.get("VAPI_API_KEY_PUBLIC", "9e22caef-b796-4b94-9100-034d30897153")
    VAPI_API_KEY_PRIVATE: str = os.environ.get("VAPI_API_KEY_PRIVATE")
    VAPI_ASSISTANT_ID: str = os.environ.get("VAPI_ASSISTANT_ID")
    GROQ_MODEL: str = "llama-3.1-8b-instant"
    # GROQ_MODEL: str = "llama-3.1-70b-versatile"


settings = Settings()
