from sqlalchemy.orm import Session
from src.models.produto import Produto
from src.schemas.produto_schema import ProdutoCreate

def criar_produto(db: Session, produto: ProdutoCreate):
    db_item = Produto(**produto.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def listar_produtos(db: Session):
    return db.query(Produto).all()

def obter_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def atualizar_produto(db: Session, produto_id: int, dados: ProdutoCreate):
    item = db.query(Produto).filter(Produto.id == produto_id).first()
    if not item:
        return None
    for key, value in dados.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def deletar_produto(db: Session, produto_id: int):
    item = db.query(Produto).filter(Produto.id == produto_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True