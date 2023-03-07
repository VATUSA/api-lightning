import datetime
from fastapi import HTTPException

from typing import Optional
from app.database.legacy.models import Solo


async def create_solo(
        id: int,
        cid: int,
        position: str,
        expires: datetime.date,
        created_at: datetime.datetime,
        updated_at: datetime.datetime) -> Solo:
    rec=Solo(
        id=id,
        cid=cid,
        position=position,
        expires=expires,
        created_at=created_at,
        updated_at=updated_at,
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

