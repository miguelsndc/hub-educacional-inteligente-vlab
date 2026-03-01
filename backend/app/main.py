from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.database import settings, engine, Base
from app.exceptions import ResourceNotFoundError, AIProviderError
from app.routers import health
from app.logger import get_logger

logger = get_logger("app.main")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hub Inteligente de Recursos Educacionais",
    description="API para gerenciamento de materiais didáticos com Smart Assist via IA.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ResourceNotFoundError)
async def not_found_handler(request: Request, exc: ResourceNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(AIProviderError)
async def ai_error_handler(request: Request, exc: AIProviderError):
    logger.warning("AI provider error", extra={"ctx_error": str(exc)})
    return JSONResponse(status_code=502, content={"detail": str(exc)})


app.include_router(health.router)


logger.info(
    "Application startup complete",
    extra={
        "ctx_environment": settings.ENVIRONMENT,
        "ctx_ai_provider": settings.AI_PROVIDER.value,
    },
)
