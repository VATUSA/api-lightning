import datetime
from typing import Optional
import pydantic


class ControllerPartial(pydantic.BaseModel):
    cid: int
    first_name: str
    last_name: str


class ControllerInfo(pydantic.BaseModel):
    cid: int
    first_name: str
    last_name: str
    facility: str
    facility_join_date: Optional[datetime.date]
    rating: int
    rating_short: str
    rating_long: str
    is_promotion_eligible: bool
    is_transfer_eligible: bool
    is_home_controller: bool
    is_visit_eligible: bool
    flag_broadcast_opt_in: bool


class CreateVisitorApplicationRequest(pydantic.BaseModel):
    facility: str
    reason: str


class RemoveVisitorStatusRequest(pydantic.BaseModel):
    facility: str
    reason: str


class UpdatePreferencesRequest(pydantic.BaseModel):
    flag_broadcast_opt_in: bool


class UpdatePreferredNameRequest(pydantic.BaseModel):
    first_name: Optional[str]
    reset: bool


