from src.database.base import Base
from sqlalchemy import Column, Integer, ForeignKey, Float, Numeric, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class ClienteProduto(Base):
    __tablename__ = "cliente_produto"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    id_produto = Column(Integer, ForeignKey("produto.id"), nullable=False)
    data_venda = Column(DateTime, default=datetime.utcnow)
    quantidade = Column(Float, nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)

    cliente = relationship("Cliente", back_populates="compras")
    funcionario = relationship("Funcionario")
    produto = relationship("Produto", back_populates="vendas")
