from src.database.base import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    salario = Column(Numeric(10, 2), nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    grupo = relationship("Usuario", back_populates="funcionarios")

    def __init__(self, nome: str, salario, id_grupo: int):
        self.nome = nome
        self.salario = salario
        self.id_grupo = id_grupo
