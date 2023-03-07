import datetime
import pydantic

from app.self.models.controller import ControllerPartial


class TrainingRecord(pydantic.BaseModel):
    student: ControllerPartial
    instructor: ControllerPartial
    session_date: datetime.datetime
    facility: str
    position: str
    duration: datetime.time
    movements: int
    score: int
    notes: str
    location: int
    ots_status: int
    ots_eval_id: int
    solo_granted: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
