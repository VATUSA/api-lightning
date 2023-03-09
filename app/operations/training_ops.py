import datetime
from typing import Optional
from app.database.legacy.models import TrainingRecord

async def edit_training_record(
        record_id: int,
        session_date: Optional[datetime.datetime],
        position: Optional[str],
        duration: Optional[str],
        movements: Optional[int],
        score: Optional[int],
        notes: Optional[str],
        location: Optional[int],
        ots_status: Optional[int],
        solo_granted: Optional[bool]) -> TrainingRecord:
    rec = await TrainingRecord.objects.get(id=record_id)
    if session_date is not None:
        await rec.update(session_date=session_date)
    if position is not None:
        await rec.update(position=position)
    if duration is not None:
        await rec.update(duration=duration)
    if movements is not None:
        await rec.update(movements=movements)
    if score is not None:
        await rec.update(score=score)
    if notes is not None:
        await rec.update(notes=notes)
    if location is not None:
        await rec.update(location=location)
    if ots_status is not None:
        await rec.update(ots_status=ots_status)
    if solo_granted is not None:
        await rec.update(solo_granted=solo_granted)
    await rec.update(updated_at=datetime.datetime.now())
    await rec.save()
    return rec

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
