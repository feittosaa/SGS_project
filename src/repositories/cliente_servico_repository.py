from sqlalchemy.orm import Session
from src.models import ClienteServico

class ClienteServicoRepository:
    def create(self, db: Session, relacao: ClienteServico):
        db.add(relacao)
        db.commit()
        db.refresh(relacao)
        return relacao

    def get_all(self, db: Session):
        return db.query(ClienteServico).all()

    def get_by_id(self, db: Session, relacao_id: int):
        return db.query(ClienteServico).filter(ClienteServico.id == relacao_id).first()

    def delete(self, db: Session, relacao: ClienteServico):
        db.delete(relacao)
        db.commit()