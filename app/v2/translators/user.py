from app.constants import rating
from app.database.legacy.models import Controller
from app.v2.models.user import User, UserRole, UserPartial


def from_controller(controller: Controller) -> User:
    return User(
        cid=controller.cid,
        fname=controller.fname,
        lname=controller.lname,
        rating=controller.rating,
        email=None,  # TODO: Fix email, only include if authorized
        facility=controller.facility,
        ratring_short=rating.short_map.get(controller.rating, "UNK"),
        created_at=controller.created_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),  # 2022-03-12T22:27:08+00:00
        updated_at=controller.updated_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        flag_needbasic=controller.flag_needbasic,
        flag_xferOverride=controller.flag_xferOverride,
        flag_broadcastOptedIn=controller.flag_broadcastOptedIn,
        facility_join=controller.facility_join.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        promotion_eligible=False,  # TODO
        transfer_eligible=False,  # TODO
        last_promotion="",  # TODO
        flag_homecontroller=controller.flag_homecontroller,
        lastactivity=controller.lastactivity.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        isMentor=len([r for r in controller.roles if r.role == 'MTR']) > 0,
        isSupIns=len([r for r in controller.roles if r.role == 'INS']) > 0,
        roles=[UserRole(
            id=r.id,
            cid=controller.cid,
            facility=r.facility,
            role=r.role,
            created_at=r.created_at.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        ) for r in controller.roles],
        visiting_facilities=[],
    )


def partial_from_controller(controller: Controller) -> UserPartial:
    return UserPartial(cid=controller.cid, fname=controller.fname, lname=controller.lname)
