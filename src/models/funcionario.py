from src.database.base import Base
from sqlalchemy import Column, Integer, String, Float

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    salario = Column(Float, nullable=False)

    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
