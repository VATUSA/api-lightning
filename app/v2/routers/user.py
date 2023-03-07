import datetime
from typing import List

from fastapi import APIRouter, Form
from app.database.legacy.models import Controller, Transfer, Promotion
from app.v2.models import training as training_models, generic as generic_models, user as user_models
from app.operations import training_ops
from app.v2.translators import user as user_translator

router = APIRouter(
    prefix="/user",
    tags=["v2/user"],
    dependencies=[],
)


@router.get('/{cid}', response_model=generic_models.DataResponse[user_models.User])
async def user_information_get(cid: int):
    user = await Controller.objects.filter(Controller.cid == cid).get_or_none()
    return generic_models.DataResponse(data=user_translator.from_controller(user)) if user is not None else None


@router.get('/{cid}/training/records', response_model=generic_models.DataResponse[List[training_models.TrainingRecord]])
async def user_training_records_list(
        cid: int
):
    # TODO
    return generic_models.DataResponse(data=[])


@router.post('/{cid}/training/record', response_model=generic_models.GenericResponse)
async def user_training_record_create(
        cid: int,
        instructor_id: int = Form(),
        facility_id: str = Form(),
        session_date: datetime.datetime = Form(),
        position: str = Form(),
        duration: str = Form(),
        movements: int = Form(),
        score: int = Form(),
        notes: str = Form(),
        location: int = Form(),
        ots_status: int = Form(),
        solo_granted: bool = Form()):
    rec = await training_ops.create_training_record(cid, instructor_id, facility_id, session_date, position, duration,
                                                    movements, score, notes, location, ots_status, solo_granted)
    return generic_models.GenericResponse(status="OK", id=rec.id)


@router.get('/{cid}/rating/history', response_model=generic_models.DataResponse[List[user_models.RatingHistory]])
async def user_rating_history_get(cid: int):
    promotions: List[Promotion] = await Promotion.objects.filter(cid=cid).all()
    return generic_models.DataResponse(data=[
        user_models.RatingHistory(
            id=p.id,
            cid=p.cid.cid,
            grantor=p.grantor,
            to=p.to,
            created_at=p.created_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            exam=p.exam.strftime("%Y-%m-%d") if p.exam is not None else None,
            examiner=p.examiner,
            position=p.position,
            **{'from': p.from_}  # This looks strange, but from is a reserved keyword and causes errors otherwise
        ) for p in promotions
    ])


@router.get('/{cid}/transfer/history', response_model=generic_models.DataResponse[List[user_models.TransferHistory]])
async def user_transfer_history_get(cid: int):
    transfers: List[Transfer] = await Transfer.objects.filter(cid=cid).all()
    return generic_models.DataResponse(data=[
        user_models.TransferHistory(
            id=t.id,
            cid=t.cid.cid,
            to=t.to,
            reason=t.reason,
            status=t.status,
            actiontext=t.actiontext,
            actionby=t.actionby,
            created_at=t.created_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            updated_at=t.updated_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            **{'from': t.from_}  # This looks strange, but from is a reserved keyword and causes errors otherwise
        ) for t in transfers])


@router.get('/filtercid/{partial_cid}', response_model=generic_models.DataResponse[List[user_models.UserPartial]])
async def user_filter_cid(partial_cid: int):
    controllers = await Controller.objects.filter(Controller.cid.contains(partial_cid)).all()
    return generic_models.DataResponse(data=[user_translator.partial_from_controller(c) for c in controllers])


@router.get('/filterlname/{partial_lname}', response_model=generic_models.DataResponse[List[user_models.UserPartial]])
async def user_filter_lname(partial_lname: str):
    controllers = await Controller.objects.filter(Controller.lname.contains(partial_lname)).all()
    return generic_models.DataResponse(data=[user_translator.partial_from_controller(c) for c in controllers])
