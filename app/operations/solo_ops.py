import datetime
from fastapi import HTTPException

from typing import Optional
from app.database.legacy.models import Solo


async def create_solo(
        cid: int,
        position: str,
        expires: datetime.date) -> Solo:
    rec=Solo(
        cid=cid,
        position=position,
        expires=expires,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    await rec.save()
    return rec

async def delete_solo(id: typing.Optional[int], cid: typing.Optional[int], position: typing.Optional[str]):
    if id is not None:
        solo = await Solo.objects.get(id=id)
        await solo.delete()
    elif cid is not None and position is not None:
        solo = await Solo.objects.get(cid=cid, position=position)
        await solo.delete()
    else:
        raise HTTPException(400, "Missing field. Must include id or cid and position")

