from typing import List

from fastapi import APIRouter
from app.v2.models import public as public_models

router = APIRouter(
    prefix="/public",
    tags=["v2/public"],
    dependencies=[],
)


@router.get('/events/{limit}', response_model=List[public_models.Event])
def events_list(limit: int = 20):
    # TODO
    return []


@router.get('/news/{limit}', response_model=List[public_models.News])
def news_list(limit: int = 20):
    # TODO
    return []


@router.get('/planes', response_model=List[public_models.Plane])
def planes_list():
    # TODO
    return []
