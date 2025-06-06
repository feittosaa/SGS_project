from sqlalchemy.orm import Session
from src.models import Servico

class ServicoRepository:
    def create(self, db: Session, servico: Servico):
        db.add(servico)
        db.commit()
        db.refresh(servico)
        return servico

    def get_all(self, db: Session):
        return db.query(Servico).all()

    def get_by_id(self, db: Session, servico_id: int):
        return db.query(Servico).filter(Servico.id == servico_id).first()

    def update(self, db: Session, servico: Servico):
        db.commit()
        db.refresh(servico)
        return servico

    def delete(self, db: Session, servico: Servico):
        db.delete(servico)
        db.commit()