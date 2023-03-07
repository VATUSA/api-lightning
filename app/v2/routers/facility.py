from typing import List, Optional
from fastapi import APIRouter, HTTPException, Form
from app.constants import rating
from app.database.legacy.models import Controller, Facility, Role, Transfer, Visit
from app.operations import roster_ops, transfer_ops
from app.v2.models import training as training_models, facility as facility_models, generic as generic_models, \
    user as user_models
from app.v2.translators import user as user_translator

router = APIRouter(
    prefix="/facility",
    tags=["v2/facility"],
    dependencies=[],
)


@router.get('/', response_model=generic_models.DataResponse[List[facility_models.FacilityPartial]])
async def facility_list_get():
    records: List[Facility] = await Facility.objects.filter(Facility.active == True).all()

    return generic_models.DataResponse(
        data=[facility_models.FacilityPartial(
            id=rec.id,
            name=rec.name,
            url=rec.url,
            region=rec.region
        ) for rec in records])


@router.get('/{facility_id}', response_model=generic_models.DataResponse[facility_models.Facility])
async def facility_info_get(facility_id: str):
    record: Facility = await Facility.objects\
        .filter(Facility.active == True)\
        .filter(Facility.id == facility_id)\
        .get_or_none()

    roles: List[Role] = await Role.objects.select_related(Role.cid).filter(Role.facility == facility_id).all()

    stat_controllers: int = await Controller.objects.filter(Controller.facility == facility_id).count()
    stat_pending_transfers: int = 0

    return generic_models.DataResponse(
        data=facility_models.Facility(
            id=record.id,
            name=record.name,
            url=record.url,
            role=[facility_models.FacilityRole(
                cid=role.cid.cid,
                name='%s %s' % (role.cid.fname, role.cid.lname),
                role=role.role
            ) for role in roles],
            stats=facility_models.FacilityStats(
                controllers=stat_controllers,
                pendingTransfers=stat_pending_transfers,
            ),
            notices={},
        ))


@router.get('/{facility_id}/roster/{membership}', response_model=generic_models.DataResponse[List[user_models.User]])
async def facility_roster_get(facility_id: str, membership: str):
    users = []
    if membership.upper() in ['HOME', 'BOTH']:
        users += await Controller.objects\
            .select_related(Controller.roles)\
            .filter(Controller.facility == facility_id)\
            .all()
    elif membership.upper() in ['VISIT', 'BOTH']:
        visitors = await Visit.objects\
            .select_related([Visit.cid, Visit.cid.roles])\
            .filter(Visit.facility == facility_id)\
            .all()
        users += [v.cid for v in visitors]
    else:
        raise HTTPException(400, "Invalid membership. Must be one of: HOME, VISIT, BOTH")
    return generic_models.DataResponse(data=[user_translator.from_controller(user) for user in users])


@router.post('/{facility_id}/roster/manageVisitor/{cid}', response_model=generic_models.GenericResponse)
async def facility_visitor_add(facility_id: str, cid: int):
    await roster_ops.add_visitor(cid, facility_id)
    # TODO
    return generic_models.GenericResponse(status='OK', testing=False)


@router.delete('/{facility_id}/roster/manageVisitor/{cid}', response_model=generic_models.GenericResponse)
async def facility_visitor_remove(facility_id: str, cid: int):
    await roster_ops.remove_visitor(cid, facility_id)
    # TODO
    return generic_models.GenericResponse(status='OK', testing=False)


@router.delete('/{facility_id}/roster/{cid}', response_model=generic_models.GenericResponse)
async def facility_roster_remove(facility_id: str, cid: int):
    await roster_ops.remove_home(cid, facility_id)
    # TODO
    return generic_models.GenericResponse(status='OK', testing=False)


@router.get('/{facility_id}/transfers',
            response_model=generic_models.DataResponse[List[facility_models.PendingTransfer]])
async def facility_transfers_list(facility_id: str):
    records = await Transfer.objects\
        .select_related(Transfer.cid)\
        .filter(Transfer.to == facility_id)\
        .filter(Transfer.status == 0)\
        .all()
    return generic_models.DataResponse(data=[
        facility_models.PendingTransfer(
            id=t.id,
            cid=t.cid.cid,
            fname=t.cid.fname,
            lname=t.cid.lname,
            reason=t.reason,
            rating=rating.short_map.get(t.cid.rating, "UNK"),
            intRating=t.cid.rating,
            date=t.created_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            fromFac=facility_models.FacilityMinimal(
                id=t.from_,
                name=""  # TODO: Fix Name
            )
        ) for t in records])


@router.put('/{facility_id}/transfers/{transfer_id}', response_model=generic_models.GenericResponse)
async def facility_transfer_edit(facility_id: str, transfer_id: int,
                                 action: str = Form(description='Valid values: accept, reject'),
                                 reason: Optional[str] = Form(), by: int = Form()):
    if action.lower() == 'accept':
        await transfer_ops.accept_transfer(transfer_id, reason, by)
    elif action.lower == 'reject':
        if reason is None:
            raise HTTPException(400, 'reason is required when action=reject')
        await transfer_ops.reject_transfer(transfer_id, reason, by)
    else:
        raise HTTPException(400, 'Invalid action. Must be one of: approve, reject')
    # TODO
    return {'status': 'OK', 'testing': False}


@router.get('/{facility_id}/training/records', response_model=generic_models.DataResponse[List[training_models.TrainingRecord]])
def facility_training_records_list(facility_id: str):
    # TODO
    return generic_models.DataResponse(data=[])
