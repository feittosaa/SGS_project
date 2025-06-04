from sqlalchemy.orm import Session
from src.models.cliente_produto import ClienteProduto
from src.schemas.cliente_produto_schema import ClienteProdutoCreate

def criar_cliente_produto(db: Session, cliente_produto: ClienteProdutoCreate):
    db_item = ClienteProduto(**cliente_produto.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

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
