from src.database.base import Base
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class ClienteServico(Base):
    __tablename__ = "cliente_servico"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id"), nullable=False)
    data_atendimento = Column(DateTime, default=datetime.utcnow)
    valor_cobrado = Column(Float, nullable=False)
    observacoes = Column(String(300), nullable=True)

    cliente = relationship("Cliente", back_populates="servicos")
    funcionario = relationship("Funcionario", back_populates="atendimentos")
    servico = relationship("Servico", back_populates="clientes")

    def __init__(self, id_cliente, id_funcionario, id_servico, valor_cobrado, observacoes=None, data_atendimento=None):
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.id_servico = id_servico
        self.valor_cobrado = valor_cobrado
        self.observacoes = observacoes
        self.data_atendimento = data_atendimento or datetime.utcnow()