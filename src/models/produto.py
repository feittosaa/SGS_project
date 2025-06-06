from src.database.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    uso_interno = Column(Boolean, default=False)
    valor = Column(Float, nullable=False)
    quantidade = Column(Float, nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="produtos")
    clientes = relationship("ClienteProduto", back_populates="produto")

    def __init__(self, nome, categoria, uso_interno, valor, quantidade, id_grupo):
        self.nome = nome
        self.categoria = categoria
        self.uso_interno = uso_interno
        self.valor = valor
        self.quantidade = quantidade
        self.id_grupo = id_grupo