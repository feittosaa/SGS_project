from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from src.database import SessionLocal
from src.models.funcionario import Funcionario
from pydantic import BaseModel

router = APIRouter()

# Schema de resposta
class FuncionarioSchema(BaseModel):
    id: int
    nome: str
    salario: float

    class Config:
        orm_mode = True

# Dependência de banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todos os funcionários
@router.get("/funcionarios", response_model=List[FuncionarioSchema])
def listar_funcionarios(db: Session = Depends(get_db)):
    return db.query(Funcionario).all()

# Rota para get um funcionário por ID
@router.get("/funcionarios/{funcionario_id}", response_model=FuncionarioSchema)
def get_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    funcionario = db.query(Funcionario).get(funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario
