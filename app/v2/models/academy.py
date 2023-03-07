from __future__ import annotations
from typing import List
import pydantic


class AcademyCourseIdentifiers(pydantic.BaseModel):
    BASIC: int
    S2: int
    S3: int
    C1: int


class AcademyTranscript(pydantic.BaseModel):
    BASIC: List[AcademyAttempt]
    S2: List[AcademyAttempt]
    S3: List[AcademyAttempt]
    C1: List[AcademyAttempt]


class AcademyAttempt(pydantic.BaseModel):
    attempt: int
    time_finished: int
    grade: int


AcademyTranscript.update_forward_refs()
