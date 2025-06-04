from src.database.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Servico(Base):
    __tablename__ = "servico"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    valor = Column(Float, nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="servicos")
    clientes = relationship("ClienteServico", back_populates="servico")

    def __init__(self, nome, categoria, valor, id_grupo):
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        self.id_grupo = id_grupo