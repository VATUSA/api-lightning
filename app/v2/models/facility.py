from __future__ import annotations

from typing import List, Dict, Optional

import pydantic


class FacilityPartial(pydantic.BaseModel):
    id: str
    name: str
    url: str
    region: int


class FacilityMinimal(pydantic.BaseModel):
    id: str
    name: str


class Facility(pydantic.BaseModel):
    id: str
    name: str
    url: str
    role: List[FacilityRole]
    stats: FacilityStats
    notices: Dict[str, List[FacilityNotice]]


class FacilityRole(pydantic.BaseModel):
    cid: int
    name: str
    role: str


class FacilityStats(pydantic.BaseModel):
    controllers: int
    pendingTransfers: int


class FacilityNotice(pydantic.BaseModel):
    id: int
    tmu_facility_id: str
    priority: int
    message: str
    expire_date: str
    created_at: str
    updated_at: str


class PendingTransfer(pydantic.BaseModel):
    id: int
    cid: int
    fname: str
    lname: str
    email: Optional[str]
    reason: str
    rating: str
    intRating: int
    date: str
    fromFac: FacilityMinimal


FacilityPartial.update_forward_refs()
Facility.update_forward_refs()
PendingTransfer.update_forward_refs()
