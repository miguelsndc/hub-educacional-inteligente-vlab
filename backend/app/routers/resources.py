from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.resource import (
    ResourceCreate,
    ResourceUpdate,
    ResourceResponse,
)
from app.schemas.common import PaginatedResponse
from app.services import resource_service
from app.constants import PAGINATION_DEFAULT_LIMIT

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("", response_model=PaginatedResponse)
def list_resources(
    page: int = Query(1, ge=1),
    limit: int = Query(PAGINATION_DEFAULT_LIMIT, ge=1),
    db: Session = Depends(get_db),
):
    return resource_service.get_all(db, page, limit)


@router.post("", response_model=ResourceResponse, status_code=201)
def create_resource(data: ResourceCreate, db: Session = Depends(get_db)):
    return resource_service.create(db, data)


@router.get("/{id}", response_model=ResourceResponse)
def get_resource(id: int, db: Session = Depends(get_db)):
    return resource_service.get_by_id(db, id)


@router.put("/{id}", response_model=ResourceResponse)
def update_resource(id: int, data: ResourceUpdate, db: Session = Depends(get_db)):
    return resource_service.update(db, id, data)


@router.delete("/{id}", status_code=204)
def delete_resource(id: int, db: Session = Depends(get_db)):
    resource_service.delete(db, id)
