from app.schemas.resource import ResourceResponse
from pydantic import BaseModel


class PaginatedResponse(BaseModel):
    items: list[ResourceResponse]
    total: int
    page: int
    limit: int
    pages: int
