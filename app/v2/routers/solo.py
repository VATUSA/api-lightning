from typing import List
import datetime
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
    rec = await solo_ops.delete_solo(id=id, cid=cid, position=position)    
    return generic_models.GenericResponse(status="OK", id=rec.id)
