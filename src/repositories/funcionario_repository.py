from sqlalchemy.orm import Session
from src.models import Funcionario
class FuncionarioRepository:
    def create(self, db: Session, funcionario: Funcionario):
        db.add(funcionario)
        db.commit()
        db.refresh(funcionario)
        return funcionario

    def get_all(self, db: Session):
        return db.query(Funcionario).all()

    def get_by_id(self, db: Session, funcionario_id: int):
        return db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()

    def update(self, db: Session, funcionario: Funcionario):
        db.commit()
        db.refresh(funcionario)
        return funcionario

    def delete(self, db: Session, funcionario: Funcionario):
        db.delete(funcionario)
        db.commit()
