from __future__ import annotations
import pydantic


class TrainingRecord(pydantic.BaseModel):
    id: int
    student_id: int
    instructor_id: int
    session_date: str
    facility_id: str
    position: str
    duration: str
    movements: int
    score: int
    notes: str
    location: int
    ots_status: bool
    is_cbt: bool
    solo_granted: bool
    modified_by: bool
