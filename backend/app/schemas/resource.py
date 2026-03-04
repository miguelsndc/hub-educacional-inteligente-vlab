from datetime import datetime

from pydantic import BaseModel, field_serializer, field_validator

from app.constants import ResourceTypeEnum
from app.models.tag import Tag


class ResourceCreate(BaseModel):
    title: str
    type: ResourceTypeEnum
    description: str | None = None
    url: str | None = None
    tags: list[str] = []

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("O título não pode ser vazio.")
        if len(value) > 255:
            raise ValueError("O título não pode ter mais de 255 caracteres.")
        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str | None) -> str | None:
        if value and len(value) > 5000:
            raise ValueError("A descrição não pode ter mais de 5000 caracteres.")
        return value

    @field_validator("url")
    @classmethod
    def validate_url(cls, value: str | None) -> str | None:
        if value and len(value) > 2048:
            raise ValueError("A URL não pode ter mais de 2048 caracteres.")
        return value

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, value: list[str]) -> list[str]:
        if len(value) > 10:
            raise ValueError("Um recurso pode ter no máximo 10 tags.")
        for tag in value:
            if len(tag.strip()) > 50:
                raise ValueError("Cada tag pode ter no máximo 50 caracteres.")
        return value


class ResourceUpdate(BaseModel):
    title: str | None = None
    type: ResourceTypeEnum | None = None
    description: str | None = None
    url: str | None = None
    tags: list[str] | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("O título não pode ser vazio.")
        if len(value) > 255:
            raise ValueError("O título não pode ter mais de 255 caracteres.")
        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str | None) -> str | None:
        if value and len(value) > 5000:
            raise ValueError("A descrição não pode ter mais de 5000 caracteres.")
        return value

    @field_validator("url")
    @classmethod
    def validate_url(cls, value: str | None) -> str | None:
        if value and len(value) > 2048:
            raise ValueError("A URL não pode ter mais de 2048 caracteres.")
        return value

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, value: list[str]) -> list[str]:
        if len(value) > 10:
            raise ValueError("Um recurso pode ter no máximo 10 tags.")
        for tag in value:
            if len(tag.strip()) > 50:
                raise ValueError("Cada tag pode ter no máximo 50 caracteres.")
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
