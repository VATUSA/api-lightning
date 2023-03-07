from fastapi import APIRouter
from app.v2.models import academy as academy_models, generic as generic_models

router = APIRouter(
    prefix="/academy",
    tags=["v2/academy"],
    dependencies=[],
)


@router.get("/identifiers", response_model=academy_models.AcademyCourseIdentifiers)
def academy_identifiers_get():
    # TODO
    return []


@router.post('/enroll/{course_id}', response_model=generic_models.GenericResponse)
def academy_enroll_post(course_id: int):
    # TODO
    return {'status': 'OK'}


@router.get('/transcript/{cid}', response_model=academy_models.AcademyTranscript)
def academy_transcript_get(cid: int):
    # TODO
    return {}
