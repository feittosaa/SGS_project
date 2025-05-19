from src.database.base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class ClienteServico(Base):
    __tablename__ = "cliente_servico"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id"), nullable=False)
    data_atendimento = Column(DateTime, default=datetime.utcnow)
    valor = Column(Numeric(10, 2), nullable=False)
    observacoes = Column(Text)

    cliente = relationship("Cliente", back_populates="servicos")
    funcionario = relationship("Funcionario")
    servico = relationship("Servico", back_populates="atendimentos")
