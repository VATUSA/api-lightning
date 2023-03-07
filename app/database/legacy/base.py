import ormar
from app.database.legacy.connection import database
from app.database.legacy.connection import metadata


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
