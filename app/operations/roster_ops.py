from typing import Optional


async def add_visitor(cid: int, facility: str):
    pass


async def remove_visitor(cid: int, facility: str):
    pass


async def remove_home(cid: int, facility: str, reason: Optional[str] = None):
    pass


async def set_user_facility(cid: int, facility: str):
    pass
