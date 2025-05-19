from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database.session import get_db
from src.schemas.funcionario_schema import *
from src.services.funcionario_service import FuncionarioService

router = APIRouter()

@router.get("/funcionarios", response_model=List[FuncionarioResponse])
def listar(db: Session = Depends(get_db)):
    return FuncionarioService(db).listar()

@router.get("/funcionarios/{id}", response_model=FuncionarioResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    funcionario = FuncionarioService(db).buscar_por_id(id)
    if not funcionario:
        raise HTTPException(404, "Funcionário não encontrado")
    return funcionario

@router.post("/funcionarios", response_model=FuncionarioResponse)
def criar(data: FuncionarioCreate, db: Session = Depends(get_db)):
    return FuncionarioService(db).criar(data)

@router.put("/funcionarios/{id}", response_model=FuncionarioResponse)
def editar(id: int, data: FuncionarioUpdate, db: Session = Depends(get_db)):
    funcionario = FuncionarioService(db).editar(id, data)
    if not funcionario:
        raise HTTPException(404, "Funcionário não encontrado")
    return funcionario

@router.delete("/funcionarios/{id}", response_model=FuncionarioResponse)
def excluir(id: int, db: Session = Depends(get_db)):
    funcionario = FuncionarioService(db).excluir(id)
    if not funcionario:
        raise HTTPException(404, "Funcionário não encontrado")
    return funcionario
