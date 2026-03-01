from fastapi import APIRouter
from sqlalchemy import text
from app.database import SessionLocal

router = APIRouter(tags=["health"])


@router.get(
    "/health",
    summary="Check API health",
    description="Endpoint para verificar se a API está funcionando corretamente.",
)
def health_check():
    """Verifica se a API e o banco estão operacionais."""
    db_status = "ok"
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
    except Exception:
        db_status = "unavailable"

    return {
        "status": "ok" if db_status == "ok" else "degraded",
        "database": db_status,
    }
