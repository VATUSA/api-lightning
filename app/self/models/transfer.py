import datetime
import pydantic


class CreateTransferRequest(pydantic.BaseModel):
    facility: str
    reason: str


class PendingTransferResponse(pydantic.BaseModel):
    to_facility: str
    from_facility: str
    reason: str
    created_at: datetime.datetime
