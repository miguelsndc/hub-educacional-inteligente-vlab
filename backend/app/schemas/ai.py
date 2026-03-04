from pydantic import BaseModel
from app.constants import ResourceTypeEnum


class AIRequest(BaseModel):
    title: str
    type: str

    def type_is_valid(self) -> bool:
        return self.type in ResourceTypeEnum


class AIResponse(BaseModel):
    description: str
    tags: list[str]
