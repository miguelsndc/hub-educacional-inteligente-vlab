from math import ceil
from sqlalchemy.orm import Session

from app.constants import PAGINATION_MAX_LIMIT
from app.exceptions import ResourceNotFoundError
from app.models.resource import Resource
from app.schemas.resource import ResourceCreate, ResourceResponse, ResourceUpdate
from app.schemas.common import PaginatedResponse


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


def get_by_id(db: Session, id: int) -> ResourceResponse:
    resource = db.query(Resource).filter(Resource.id == id).first()
    if not resource:
        raise ResourceNotFoundError(id)
    return ResourceResponse.model_validate(resource)


def create(db: Session, data: ResourceCreate) -> ResourceResponse:
    resource = Resource(**data.model_dump())
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return ResourceResponse.model_validate(resource)


def update(db: Session, id: int, data: ResourceUpdate) -> ResourceResponse:
    resource = get_by_id(db, id)

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(resource, field, value)

    db.commit()
    db.refresh(resource)
    return ResourceResponse.model_validate(resource)


def delete(db: Session, id: int) -> None:
    resource = get_by_id(db, id)
    db.delete(resource)
    db.commit()
