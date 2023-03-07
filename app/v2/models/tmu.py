from __future__ import annotations

from typing import List

import pydantic


class TMUNotice(pydantic.BaseModel):
    id: int
    tmu_facility: List[TMUFacility]
    priority: str
    message: str
    expire_date: str
    start_date: str
    is_delay: bool
    is_pref_route: bool


class TMUFacility(pydantic.BaseModel):
    id: str
    name: str
    parent: str


TMUNotice.update_forward_refs()
