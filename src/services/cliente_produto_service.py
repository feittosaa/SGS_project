from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.cliente_produto import ClienteProduto
from src.models.produto import Produto
from src.schemas.cliente_produto_schema import ClienteProdutoCreate

def criar_cliente_produto(db: Session, cliente_produto: ClienteProdutoCreate):
    produto = db.query(Produto).filter(Produto.id == cliente_produto.id_produto).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if produto.quantidade< cliente_produto.quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    produto.quantidade -= cliente_produto.quantidade

    db_item = ClienteProduto(**cliente_produto.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def listar_clientes_produtos(db: Session):
    return db.query(ClienteProduto).all()

def obter_cliente_produto(db: Session, cliente_produto_id: int):
    return db.query(ClienteProduto).filter(ClienteProduto.id == cliente_produto_id).first()

def atualizar_cliente_produto(db: Session, cliente_produto_id: int, dados: ClienteProdutoCreate):
    item = db.query(ClienteProduto).filter(ClienteProduto.id == cliente_produto_id).first()
    if not item:
        return None
    for key, value in dados.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def deletar_cliente_produto(db: Session, cliente_produto_id: int):
    item = db.query(ClienteProduto).filter(ClienteProduto.id == cliente_produto_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
