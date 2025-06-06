from sqlalchemy.orm import Session
from src.models import Cliente

class ClienteRepository:
    def create(self, db: Session, cliente: Cliente):
        db.add(cliente)
        db.commit()
        db.refresh(cliente)
        return cliente

    def get_all(self, db: Session):
        return db.query(Cliente).all()

    def get_by_id(self, db: Session, cliente_id: int):
        return db.query(Cliente).filter(Cliente.id == cliente_id).first()

    def update(self, db: Session, cliente: Cliente):
        db.commit()
        db.refresh(cliente)
        return cliente

    def delete(self, db: Session, cliente: Cliente):
        db.delete(cliente)
        db.commit()