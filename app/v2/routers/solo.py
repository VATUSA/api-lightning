from typing import List

from fastapi import APIRouter
from app.v2.models import solo as solo_models, generic as generic_models

router = APIRouter(
    prefix="/solo",
    tags=["v2/solo"],
    dependencies=[],
)


@router.get('/', response_model=List[solo_models.Solo])
async def solo_list():
    # TODO
    return []


@router.post('/', response_model=generic_models.GenericResponse)
async def solo_create():
    # TODO
    return {'status': 'OK', 'testing': False}


@router.delete('/', response_model=generic_models.GenericResponse)
async def solo_delete():
    # TODO
    return {'status': 'OK', 'testing': False}
