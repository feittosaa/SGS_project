from sqlalchemy.orm import Session
from src.models.funcionario import Funcionario

class FuncionarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Funcionario).all()

    def get_by_id(self, funcionario_id: int):
        return self.db.query(Funcionario).get(funcionario_id)

    def create(self, funcionario: Funcionario):
        self.db.add(funcionario)
        self.db.commit()
        self.db.refresh(funcionario)
        return funcionario

    def update(self, db_funcionario: Funcionario, data: dict):
        for key, value in data.items():
            setattr(db_funcionario, key, value)
        self.db.commit()
        return db_funcionario

    def delete(self, funcionario: Funcionario):
        self.db.delete(funcionario)
        self.db.commit()
