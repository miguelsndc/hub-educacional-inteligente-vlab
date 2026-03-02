from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import ai_service
from app.database import get_db
from app.schemas.ai import AIRequest, AIResponse

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/suggest", response_model=AIResponse)
def suggest(request: AIRequest, db: Session = Depends(get_db)):
    return ai_service.suggest(request, db)
