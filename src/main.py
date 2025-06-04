from fastapi import FastAPI
from src.controllers import (
    usuario_controller,
    cliente_controller,
    produto_controller,
    servico_controller,
    funcionario_controller,
    cliente_produto_controller,
    cliente_servico_controller
)
from src.database.base import Base
from src.database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SGS API",
    version="1.0.0"
)

# Rotas
app.include_router(usuario_controller.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(cliente_controller.router, prefix="/clientes", tags=["Clientes"])
app.include_router(produto_controller.router, prefix="/produtos", tags=["Produtos"])
app.include_router(servico_controller.router, prefix="/servicos", tags=["Serviços"])
app.include_router(funcionario_controller.router, prefix="/funcionarios", tags=["Funcionários"])
app.include_router(cliente_produto_controller.router, prefix="/clientes-produtos", tags=["Clientes-Produtos"])
app.include_router(cliente_servico_controller.router, prefix="/clientes-servicos", tags=["Clientes-Serviços"])
