from __future__ import annotations
from typing import Optional, List
import pydantic


class User(pydantic.BaseModel):
    cid: int
    fname: str
    lname: str
    email: Optional[str]
    facility: str
    rating: int
    ratring_short: str
    created_at: str
    updated_at: str
    flag_needbasic: int
    flag_xferOverride: int
    flag_broadcastOptedIn: int
    flag_preventStaffAssign: Optional[int]
    facility_join: str
    promotion_eligible: bool
    transfer_eligible: bool
    last_promotion: str
    flag_homecontroller: bool
    lastactivity: str
    isMentor: bool
    isSupIns: bool
    roles: List[UserRole]
    visiting_facilities: List[VisitingFacility]


class UserRole(pydantic.BaseModel):
    id: int
    cid: int
    facility: str
    role: str
    created_at: str


class VisitingFacility(pydantic.BaseModel):
    id: str
    name: str
    region: int


class UserPartial(pydantic.BaseModel):
    cid: int
    fname: str
    lname: str


class RatingHistory(pydantic.BaseModel):
    id: int
    cid: int
    grantor: int
    to: int
    from_: int = pydantic.Field(alias="from")
    created_at: str
    exam: Optional[str]
    examiner: int
    position: str


class TransferHistory(pydantic.BaseModel):
    id: int
    cid: int
    to: str
    from_: str = pydantic.Field(alias="from")
    reason: str
    status: int
    actiontext: str
    actionby: int
    created_at: str
    updated_at: str


# Keep update_forward_refs() calls at the bottom of the file

User.update_forward_refs()
