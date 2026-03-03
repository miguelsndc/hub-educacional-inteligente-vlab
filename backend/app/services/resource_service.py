from math import ceil
from sqlalchemy.orm import Session

from app.constants import PAGINATION_MAX_LIMIT
from app.exceptions import ResourceNotFoundError
from app.models.resource import Resource
from app.models.tag import Tag
from app.schemas.resource import ResourceCreate, ResourceResponse, ResourceUpdate
from app.schemas.common import PaginatedResponse


def _get_or_create_tag(db: Session, name: str):
    normalized = name.strip().lower()
    tag = db.query(Tag).filter(Tag.name == normalized).first()
    if not tag:
        tag = Tag(name=normalized)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag


def _resolve_tags(db: Session, tag_names: list[str]) -> list[Tag]:
    return [_get_or_create_tag(db, name) for name in tag_names]


def get_all(db: Session, page: int, limit: int) -> PaginatedResponse:
    limit = min(limit, PAGINATION_MAX_LIMIT)
    offset = (page - 1) * limit
    total = db.query(Resource).count()
    resources = db.query(Resource).offset(offset).limit(limit).all()
    return PaginatedResponse(
        items=[ResourceResponse.model_validate(r) for r in resources],
        total=total,
        page=page,
        limit=limit,
        pages=ceil(total / limit) if total > 0 else 1,
    )


def _get_by_id(db: Session, id: int) -> Resource:
    resource = db.query(Resource).filter(Resource.id == id).first()
    if not resource:
        raise ResourceNotFoundError(id)
    return resource  

def get_by_id(db: Session, id: int) -> ResourceResponse:
    return ResourceResponse.model_validate(_get_by_id(db, id))

def create(db: Session, data: ResourceCreate) -> ResourceResponse:
    resource = Resource(
        title=data.title,
        description=data.description,
        type=data.type,
        url=data.url,
        tags=_resolve_tags(db, data.tags),
    )
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return ResourceResponse.model_validate(resource)


def update(db: Session, id: int, data: ResourceUpdate) -> ResourceResponse:
    resource = _get_by_id(db, id)

    for field, value in data.model_dump(exclude_unset=True, exclude={"tags"}).items():
        setattr(resource, field, value)

    if data.tags is not None:
        resource.tags = _resolve_tags(db, data.tags)

    db.commit()
    db.refresh(resource)
    return ResourceResponse.model_validate(resource)


def delete(db: Session, id: int) -> None:
    resource = _get_by_id(db, id)
    db.delete(resource)
    db.commit()
