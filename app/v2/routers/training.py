from fastapi import APIRouter
from app.database.legacy.models import TrainingRecord
from app.v2.models import training as training_models, generic as generic_models
from app.operations import training_ops
import datetime

router = APIRouter(
    prefix="/training",
    tags=["v2/training"],
    dependencies=[],
)


@router.get('/record/{record_id}', response_model=generic_models.DataResponse[List[training_models.TrainingRecord]])
async def training_record_get(record_id: int):
    record = await TrainingRecord.objects.get(id=record_id)
    return generic_models.DataResponse(data=
        training_models.TrainingRecord(
            id = record.id,
            student_id = record.student_id,
            instructor_id = record.instructor_id,
            session_date = record.session_date,
            facility_id = record.facility_id,
            position = record.position,
            duration = record.duration,
            movements = record.movements,
            score = record.score,
            notes = record.notes,
            location = record.location,
            ots_stats = record.ots_status,
            is_cbt = record.is_cbt,
            solo_granted = record.solo_granted,
            modified_by = record.modified_by
        )
    )


@router.put('/record/{record_id}', response_model=generic_models.GenericResponse)
async def training_record_edit(
    record_id: int,
    session_date: datetime.datetime = Form(),
    position: str = Form(),
    duration: datetime.time = Form(),
    movements: int = Form(),
    score: int = Form(),
    notes: str = Form(),
    location: int = Form(),
    ots_status: int = Form(),
    solo_granted: bool = Form()):
    if not re.match(r"^([A-Z0-9]{2,3})_(DEL|GND|TWR|APP|DEP|CTR)$", position):
        raise HTTPException(400, "Invalid position. Must be a valid position")
    if score not in range(1, 6):
        raise HTTPException(400, "Invalid score. Must be integer 1-5")
    if location not in range(0, 3):
        raise HTTPException(400, "Invalid location. Must be integer 0-2")
    if ots_status not in range(0, 4):
        raise HTTPException(400, "Invalid ots_status. Must be integer 0-3")
    rec = await training_ops.edit_training_record(
        record_id=record_id,
        session_date=session_date,
        position=position,
        duration=duration,
        movements=movements,
        score=score,
        notes=notes,
        location=location,
        ots_status=ots_status,
        solo_granted=solo_granted
    )
    return generic_models.GenericResponse(status="OK", id=rec.id)


@router.delete('/record/{record_id}', response_model=generic_models.GenericResponse)
async def training_record_delete(record_id: int):
    rec = await TrainingRecord.objects.get(id=record_id)
    await rec.delete()
    return {'status': 'OK', 'testing': False}
