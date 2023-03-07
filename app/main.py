from fastapi import FastAPI
from app.database.legacy import connection as legacy_connection
from app.v2 import v2_app
from app.v3 import v3_app


app = FastAPI()

app.mount('/v2', v2_app)
app.mount('/v3', v3_app)

legacy_connection.attach(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}
