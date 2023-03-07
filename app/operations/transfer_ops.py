from typing import Optional


async def create_transfer(cid: int, facility: str, reason: Optional[str] = None):
    pass


async def accept_transfer(transfer_id: int, reason: Optional[str], by_cid: int):
    pass


async def reject_transfer(transfer_id: int, reason: str, by_cid: int):
    pass
