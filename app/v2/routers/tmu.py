from typing import List

from fastapi import APIRouter
from app.v2.models import generic as generic_models, tmu as tmu_models

router = APIRouter(
    prefix="/tmu",
    tags=["v2/tmu"],
    dependencies=[],
)


@router.get('/notices/{tmufacid}', response_model=List[tmu_models.TMUNotice])
def notices_list(tmufacid: str):
    # TODO
    return []


@router.get('/notice/{notice_id}', response_model=tmu_models.TMUNotice)
def notice_info(notice_id: int):
    # TODO
    return []


@router.post('/notice', response_model=generic_models.GenericResponse)
def notice_create():
    # TODO
    return {'status': 'OK', 'testing': False}


@router.put('/notice/{notice_id}', response_model=generic_models.GenericResponse)
def notice_edit(notice_id: int):
    # TODO
    return {'status': 'OK', 'testing': False}


@router.delete('/notice/{notice_id}', response_model=generic_models.GenericResponse)
def notice_delete(notice_id: int):
    # TODO
    return {'status': 'OK', 'testing': False}
