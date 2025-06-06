from sqlalchemy.orm import Session
from src.models import ClienteProduto

class ClienteProdutoRepository:
    def create(self, db: Session, relacao: ClienteProduto):
        db.add(relacao)
        db.commit()
        db.refresh(relacao)
        return relacao

    def get_all(self, db: Session):
        return db.query(ClienteProduto).all()

    def get_by_id(self, db: Session, relacao_id: int):
        return db.query(ClienteProduto).filter(ClienteProduto.id == relacao_id).first()

    def delete(self, db: Session, relacao: ClienteProduto):
        db.delete(relacao)
        db.commit()