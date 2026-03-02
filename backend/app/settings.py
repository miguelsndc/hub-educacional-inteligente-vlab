from pydantic_settings import BaseSettings
from app.constants import AIProviderEnum, AI_DEFAULT_PROVIDER, AI_DEFAULT_TIMEOUT


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    AI_PROVIDER: AIProviderEnum = AI_DEFAULT_PROVIDER
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.0-flash"
    ANTHROPIC_API_KEY: str = ""
    AI_TIMEOUT_SECONDS: int = AI_DEFAULT_TIMEOUT
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: str = "https://localhost:5173"

    model_config = {"env_file": ".env", "extra": "ignore"}

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",")]


settings = Settings()
