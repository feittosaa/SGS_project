from fastapi import FastAPI
from src.routes.endpoints import router
from src.database.base import Base
from src.database.session import engine

app = FastAPI(title="SGS API")

app.include_router(router, prefix="/api")
