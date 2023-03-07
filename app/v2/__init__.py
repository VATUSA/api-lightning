from fastapi import FastAPI
from .routers import tmu, solo, user, facility, public, academy, training

v2_app = FastAPI()

v2_app.include_router(academy.router)
v2_app.include_router(facility.router)
v2_app.include_router(public.router)
v2_app.include_router(solo.router)
v2_app.include_router(tmu.router)
v2_app.include_router(training.router)
v2_app.include_router(user.router)
