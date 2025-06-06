from src.database.base import Base
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class ClienteServico(Base):
    __tablename__ = "cliente_servico"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id", ondelete="CASCADE"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id", ondelete="CASCADE"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id", ondelete="CASCADE"), nullable=False)
    data_atendimento = Column(DateTime, default=datetime.utcnow)
    valor = Column(Float, nullable=False)
    observacoes = Column(String(300), nullable=True)

    cliente = relationship("Cliente", back_populates="servicos", passive_deletes=True)
    funcionario = relationship("Funcionario", back_populates="atendimentos", passive_deletes=True)
    servico = relationship("Servico", back_populates="clientes", passive_deletes=True)

    def __init__(self, id_cliente, id_funcionario, id_servico, valor, observacoes=None, data_atendimento=None):
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.id_servico = id_servico
        self.valor = valor
        self.observacoes = observacoes
        self.data_atendimento = data_atendimento or datetime.utcnow()