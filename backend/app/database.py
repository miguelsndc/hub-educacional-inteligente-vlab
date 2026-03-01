from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pydantic_settings import BaseSettings
from app.constants import AIProvider, AI_DEFAULT_PROVIDER, AI_DEFAULT_TIMEOUT


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    AI_PROVIDER: AIProvider = AI_DEFAULT_PROVIDER
    GEMINI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    AI_TIMEOUT_SECONDS: int = AI_DEFAULT_TIMEOUT
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: str = "https://localhost:5173"

    model_config = {"env_file": ".env", "extra": "ignore"}

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",")]


settings = Settings()

connection_args = (
    {"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

engine = create_engine(settings.DATABASE_URL, connect_args=connection_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
