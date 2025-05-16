from fastapi import FastAPI
from src.routes.funcionario_routes import router as funcionario_router

app = FastAPI(title="SGS")

# Inclui as rotas no app
app.include_router(funcionario_router, prefix="/api")
