from sqlalchemy.orm import Session
from src.models import Produto

class ProdutoRepository:
    def create(self, db: Session, produto: Produto):
        db.add(produto)
        db.commit()
        db.refresh(produto)
        return produto

    def get_all(self, db: Session):
        return db.query(Produto).all()

    def get_by_id(self, db: Session, produto_id: int):
        return db.query(Produto).filter(Produto.id == produto_id).first()

    def update(self, db: Session, produto: Produto):
        db.commit()
        db.refresh(produto)
        return produto

    def delete(self, db: Session, produto: Produto):
        db.delete(produto)
        db.commit()
