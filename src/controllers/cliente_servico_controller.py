from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.cliente_servico_schema import ClienteServicoCreate, ClienteServicoRead
from src.database.session import get_db
from src.services import cliente_servico_service

router = APIRouter(tags=["Clientes-Serviços"])

@router.post("/", response_model=ClienteServicoRead)
def criar_cliente_servico(cliente_servico: ClienteServicoCreate, db: Session = Depends(get_db)):
    return cliente_servico_service.criar_cliente_servico(db, cliente_servico)

@router.get("/", response_model=list[ClienteServicoRead])
def listar_clientes_servicos(db: Session = Depends(get_db)):
    return cliente_servico_service.listar_clientes_servicos(db)

@router.get("/{cliente_servico_id}", response_model=ClienteServicoRead)
def obter_cliente_servico(cliente_servico_id: int, db: Session = Depends(get_db)):
    item = cliente_servico_service.obter_cliente_servico(db, cliente_servico_id)
    if not item:
        raise HTTPException(status_code=404, detail="ClienteServico não encontrado")
    return item

@router.put("/{cliente_servico_id}", response_model=ClienteServicoRead)
def atualizar_cliente_servico(cliente_servico_id: int, dados: ClienteServicoCreate, db: Session = Depends(get_db)):
    item = cliente_servico_service.atualizar_cliente_servico(db, cliente_servico_id, dados)
    if not item:
        raise HTTPException(status_code=404, detail="ClienteServico não encontrado")
    return item

@router.delete("/{cliente_servico_id}")
def deletar_cliente_servico(cliente_servico_id: int, db: Session = Depends(get_db)):
    sucesso = cliente_servico_service.deletar_cliente_servico(db, cliente_servico_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="ClienteServico não encontrado")
    return {"detail": "ClienteServico deletado com sucesso"}