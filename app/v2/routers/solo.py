from typing import List
import datetime
import re
from fastapi import APIRouter
from app.database.legacy.models import Solo
from app.operations import solo_ops
from app.v2.models import solo as solo_models, generic as generic_models

router = APIRouter(
    prefix="/solo",
    tags=["v2/solo"],
    dependencies=[],
)


@router.get('/', response_model=generic_models.DataResponse[List[solo_models.Solo]])
async def solo_list():
    solos: List[Solo] = await Solo.objects.all() 
    return generic_models.DataResponse(data=[
        solo_models.Solo(
            id=s.id,
            cid=s.cid,
            position=s.position,
            expires=s.expires,
            created_at=s.created_at,
            updated_at=s.updated_at,
            **{'from': s.from_}
        
        ) for s in solos
    ])

@router.post('/', response_model=generic_models.GenericResponse)
async def solo_create(
        cid: int = Form(),
        position: str = Form(),
        expires: datetime.date = Form()):
    if datetime.date.today() - expires > 30:
         raise HTTPException(400, "Invalid expiration date. Solo certification can last a maximum of 30 days")
    if not re.match(r"^([A-Z0-9]{2,3})_(APP|CTR)$", position):
        raise HTTPException(400, "Invalid position. Must be valid TRACON/Enroute position")
    rec = await solo_ops.create_solo(
        cid=cid,
        position=position,
        expires=expires
    )
    return generic_models.GenericResponse(status="OK", id=rec.id)
       
       


@router.delete('/', response_model=generic_models.GenericResponse)
async def solo_delete(
        id: int = Form(),
        cid: int = Form(),
        position: str = Form()):
    if id is not None: 
        rec = await solo_ops.delete_solo(id)    
    elif cid is not None and position is not None:
        solo = await Solo.objects.get(cid=cid, position=position)
        rec = await solo_ops.delete_solo(solo.id)    
    else:
        raise HTTPException(400, "Missing field. Must include id or cid and position")

    return generic_models.GenericResponse(status="OK", id=rec.id)
