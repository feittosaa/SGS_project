from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.cliente_produto_schema import ClienteProdutoCreate, ClienteProdutoRead
from src.database.session import get_db
from src.services import cliente_produto_service

router = APIRouter(tags=["Clientes-Produtos"])

@router.post("/", response_model=ClienteProdutoRead)
def criar_cliente_produto(cliente_produto: ClienteProdutoCreate, db: Session = Depends(get_db)):
    return cliente_produto_service.criar_cliente_produto(db, cliente_produto)

@router.get("/{cliente_produto_id}", response_model=ClienteProdutoRead)
def obter_cliente_produto(cliente_produto_id: int, db: Session = Depends(get_db)):
    item = cliente_produto_service.obter_cliente_produto(db, cliente_produto_id)
    if not item:
        raise HTTPException(status_code=404, detail="ClienteProduto não encontrado")
    return item

@router.put("/{cliente_produto_id}", response_model=ClienteProdutoRead)
def atualizar_cliente_produto(cliente_produto_id: int, dados: ClienteProdutoCreate, db: Session = Depends(get_db)):
    item = cliente_produto_service.atualizar_cliente_produto(db, cliente_produto_id, dados)
    if not item:
        raise HTTPException(status_code=404, detail="ClienteProduto não encontrado")
    return item

@router.delete("/{cliente_produto_id}")
def deletar_cliente_produto(cliente_produto_id: int, db: Session = Depends(get_db)):
    sucesso = cliente_produto_service.deletar_cliente_produto(db, cliente_produto_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="ClienteProduto não encontrado")
    return {"detail": "ClienteProduto deletado com sucesso"}
