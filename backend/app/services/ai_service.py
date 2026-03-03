from sqlalchemy.orm import Session

from app.models.tag import Tag
from app.providers.factory import get_provider
from app.schemas.ai import AIResponse, AIRequest
from app.settings import settings


def _load_prompt() -> str:
    with open("app/prompts/pedagogical_assistant.txt", "r") as f:
        return f.read()


def _get_existing_tags(db: Session) -> list[str]:
    return [tag.name for tag in db.query(Tag).all()]


def suggest(request: AIRequest, db: Session) -> AIResponse:
    provider = get_provider(settings)

    existing_tags = _get_existing_tags(db)
    prompt = _load_prompt()

    user_msg = {
        f"Título: {request.title}\n",
        f"Tags existentes: {', '.join(existing_tags) if existing_tags else 'Nenhuma'}\n",
    }

    return provider.suggest(prompt=prompt, user_message=user_msg, title=request.title)
