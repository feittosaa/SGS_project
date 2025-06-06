from src.database.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    salario = Column(Float, nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="funcionarios")
    vendas_produto = relationship(
        "ClienteProduto",
        back_populates="funcionario",
        cascade="all, delete",
        passive_deletes=True
    )
    atendimentos = relationship(
        "ClienteServico",
        back_populates="funcionario",
        cascade="all, delete",
        passive_deletes=True
    )

    def __init__(self, nome, salario, id_grupo):
        self.nome = nome
        self.salario = salario
        self.id_grupo = id_grupo