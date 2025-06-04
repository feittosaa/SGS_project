from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.servico_schema import ServicoCreate, ServicoRead
from src.database.session import get_db
from src.services import servico_service

router = APIRouter(tags=["Serviços"])

@router.post("/", response_model=ServicoRead)
def criar_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    return servico_service.criar_servico(db, servico)

@router.get("/{servico_id}", response_model=ServicoRead)
def obter_servico(servico_id: int, db: Session = Depends(get_db)):
    item = servico_service.obter_servico(db, servico_id)
    if not item:
        raise HTTPException(status_code=404, detail="Servico não encontrado")
    return item

@router.put("/{servico_id}", response_model=ServicoRead)
def atualizar_servico(servico_id: int, dados: ServicoCreate, db: Session = Depends(get_db)):
    item = servico_service.atualizar_servico(db, servico_id, dados)
    if not item:
        raise HTTPException(status_code=404, detail="Servico não encontrado")
    return item

@router.delete("/{servico_id}")
def deletar_servico(servico_id: int, db: Session = Depends(get_db)):
    sucesso = servico_service.deletar_servico(db, servico_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Servico não encontrado")
    return {"detail": "Servico deletado com sucesso"}