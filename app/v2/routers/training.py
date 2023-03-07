from fastapi import APIRouter
from app.v2.models import training as training_models, generic as generic_models

router = APIRouter(
    prefix="/training",
    tags=["v2/training"],
    dependencies=[],
)


@router.get('/record/{record_id}', response_model=training_models.TrainingRecord)
def training_record_get(record_id: int):
    # TODO
    return {}


@router.put('/record/{record_id}', response_model=generic_models.GenericResponse)
def training_record_edit(record_id: int):
    # TODO
    return {'status': 'OK', 'testing': False}


@router.delete('/record/{record_id}', response_model=generic_models.GenericResponse)
def training_record_delete(record_id: int):
    # TODO
    return {'status': 'OK', 'testing': False}
