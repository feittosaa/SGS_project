from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.cliente_schema import ClienteCreate, ClienteRead, ClienteHistoricoSchema
from src.database.session import get_db
from src.services import cliente_service
from src.models.cliente import Cliente

router = APIRouter(tags=["Clientes"])

@router.post("/", response_model=ClienteRead)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.criar_cliente(db, cliente)

@router.get("/", response_model=list[ClienteRead])
def listar_clientes(db: Session = Depends(get_db)):
    return cliente_service.listar_clientes(db)

@router.get("/{cliente_id}", response_model=ClienteRead)
def obter_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = cliente_service.obter_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.put("/{cliente_id}", response_model=ClienteRead)
def atualizar_cliente(cliente_id: int, dados: ClienteCreate, db: Session = Depends(get_db)):
    cliente = cliente_service.atualizar_cliente(db, cliente_id, dados)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    sucesso = cliente_service.deletar_cliente(db, cliente_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"detail": "Cliente deletado com sucesso"}

@router.get("/{cliente_id}/historico", response_model=ClienteHistoricoSchema)
def obter_historico(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {
        "produtos": cliente.produtos,
        "servicos": cliente.servicos
    }

