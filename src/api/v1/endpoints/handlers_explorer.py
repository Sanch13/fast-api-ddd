from fastapi import APIRouter

import src.apps.animal.fake.explorer as service
from src.apps.animal.infrastructure.model.explorer import Explorer

router = APIRouter(prefix="/explorer", tags=["explorer"])


@router.get("/")
def get_all_explorers() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_explorer_by_name(name: str) -> Explorer | None:
    return service.get_one(name=name)
