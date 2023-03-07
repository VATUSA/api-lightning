from __future__ import annotations
import pydantic


class Solo(pydantic.BaseModel):
    id: int
    cid: int
    lastname: str
    firstname: str
    position: str
    expDate: str
