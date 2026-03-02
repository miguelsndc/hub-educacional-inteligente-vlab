from pydantic import BaseModel
from app.constants import RESOURCE_TYPES


class AIRequest(BaseModel):
    title: str
    type: str

    def type_is_valid(self) -> bool:
        return self.type in RESOURCE_TYPES


class AIResponse(BaseModel):
    description: str
    tags: list[str]
