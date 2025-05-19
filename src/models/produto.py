from src.database.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Numeric, Float, ForeignKey
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    uso_interno = Column(Boolean, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    quantidade = Column(Float, nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    grupo = relationship("Usuario", back_populates="produtos")
    vendas = relationship("ClienteProduto", back_populates="produto")
