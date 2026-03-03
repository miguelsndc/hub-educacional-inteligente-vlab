from datetime import datetime

from pydantic import BaseModel, field_serializer, field_validator

from app.constants import RESOURCE_TYPES
from app.models.tag import Tag


class ResourceCreate(BaseModel):
    title: str
    type: str
    description: str | None = None
    url: str | None = None
    tags: list[str] = []

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

    @field_validator("type")
    @classmethod
    def validate_type(cls, value):
        if value not in RESOURCE_TYPES:
            raise ValueError(f"Type must be one of: {', '.join(RESOURCE_TYPES)}")
        return value


class ResourceUpdate(BaseModel):
    title: str | None = None
    type: str | None = None
    description: str | None = None
    url: str | None = None
    tags: list[str] | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Title cannot be empty")
        return value

    @field_validator("type")
    @classmethod
    def validate_type(cls, value):
        if value is not None and value not in RESOURCE_TYPES:
            raise ValueError(f"Type must be one of: {', '.join(RESOURCE_TYPES)}")
        return value


class ResourceResponse(BaseModel):
    id: int
    title: str
    type: str
    description: str | None
    url: str | None
    tags: list
    created_at: datetime
    updated_at: datetime

    @field_serializer("tags")
    def serialize_tags(self, value: list) -> list[str]:
        return [tag.name if isinstance(tag, Tag) else tag for tag in value]

    model_config = {"from_attributes": True}
