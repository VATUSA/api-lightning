from __future__ import annotations
import pydantic


class Event(pydantic.BaseModel):
    id_event: int
    start_date: str
    end_date: str
    id_board: int
    id_topic: int
    title: str
    id_member: int


class News(pydantic.BaseModel):
    id_msg: int
    id_topic: int
    id_board: int
    poster_time: int
    id_member: int
    id_msg_modified: int
    subject: str
    poster_name: int
    poster_email: str
    poster_ip: str
    smileys_enabled: int
    modified_time: int
    modified_name: str
    body: str
    icon: str
    approved: int


class Plane(pydantic.BaseModel):
    callsign: str
    cid: int
    type: str
    dep: str
    arr: str
    route: str
    lat: int
    lon: int
    hdg: int
    spd: int
    alt: int

