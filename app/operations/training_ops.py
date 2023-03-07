import datetime
from app.database.legacy.models import TrainingRecord


async def create_training_record(
        student_cid: int,
        instructor_cid: int,
        facility_id: str,
        session_date: datetime.datetime,
        position: str,
        duration: str,
        movements: int,
        score: int,
        notes: str,
        location: int,
        ots_status: int,
        solo_granted: bool) -> TrainingRecord:
    rec = TrainingRecord(
        student_id=student_cid,
        instructor_id=instructor_cid,
        session_date=session_date,
        facility_id=facility_id,
        position=position,
        duration=duration,
        movements=movements,
        score=score,
        notes=notes,
        location=location,
        ots_status=ots_status,
        ots_eval_id=None,
        is_cbt=False,
        solo_granted=solo_granted,
        created_at=datetime.datetime.now(),
        updated_at=None,
    )
    await rec.save()
    return rec
