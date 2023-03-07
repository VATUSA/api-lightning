from typing import Optional
from app.database.legacy.models import Facility


def valid_api_key(key: str, fac: Optional[str] = None):
    if key is None or key == '':
        return False
    if fac is not None:
        fac = fac.upper()

    facility = Facility.objects.filter((Facility.apikey == key) | (Facility.api_sandbox_key == key)).get_or_none()

    # Inter - ARTCC Visiting Agreements - Allow Data Retrieval
    exceptions = {
        'ZTL': ['ZHU', 'ZJX'],
        'ZHU': ['ZTL', 'ZJX'],
        'ZJX': ['ZHU', 'ZTL'],
    }
    if facility is not None:
        if fac is None:
            return True
        elif fac == facility.id:
            return True
        elif facility.id in exceptions.get(fac, []):
            return True

    return False
