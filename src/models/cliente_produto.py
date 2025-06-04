from src.database.base import Base
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class ClienteProduto(Base):
    __tablename__ = "cliente_produto"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    id_produto = Column(Integer, ForeignKey("produto.id"), nullable=False)
    data_venda = Column(DateTime, default=datetime.utcnow)
    valor_total = Column(Float, nullable=False)
    quantidade = Column(Float, nullable=False)

    cliente = relationship("Cliente", back_populates="produtos")
    funcionario = relationship("Funcionario", back_populates="vendas_produto")
    produto = relationship("Produto", back_populates="clientes")

    def __init__(self, id_cliente, id_funcionario, id_produto, valor_total, quantidade, data_venda=None):
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.id_produto = id_produto
        self.valor_total = valor_total
        self.quantidade = quantidade
        self.data_venda = data_venda or datetime.utcnow()