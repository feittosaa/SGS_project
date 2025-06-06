from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.funcionario_schema import FuncionarioCreate, FuncionarioRead
from src.database.session import get_db
from src.services import funcionario_service

router = APIRouter(tags=["Funcionários"])

@router.post("/", response_model=FuncionarioRead)
def criar_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    return funcionario_service.criar_funcionario(db, funcionario)

@router.get("/", response_model=list[FuncionarioRead])
def listar_funcionarios(db: Session = Depends(get_db)):
    return funcionario_service.listar_funcionarios(db)

@router.get("/{funcionario_id}", response_model=FuncionarioRead)
def obter_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    item = funcionario_service.obter_funcionario(db, funcionario_id)
    if not item:
        raise HTTPException(status_code=404, detail="Funcionario não encontrado")
    return item

@router.put("/{funcionario_id}", response_model=FuncionarioRead)
def atualizar_funcionario(funcionario_id: int, dados: FuncionarioCreate, db: Session = Depends(get_db)):
    item = funcionario_service.atualizar_funcionario(db, funcionario_id, dados)
    if not item:
        raise HTTPException(status_code=404, detail="Funcionario não encontrado")
    return item

@router.delete("/{funcionario_id}")
def deletar_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    sucesso = funcionario_service.deletar_funcionario(db, funcionario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Funcionario não encontrado")
    return {"detail": "Funcionario deletado com sucesso"}