
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
from app import models
from app.routers.child import router as child_router
from app.routers.registration import router as registration_router
from app.routers.auth import router as auth_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="AVEN API",
    description="School journey visibility prototype",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(child_router)
app.include_router(registration_router)
app.include_router(auth_router)

