from src.database.base import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

class Servico(Base):
    __tablename__ = "servico"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    grupo = relationship("Usuario", back_populates="servicos")
    atendimentos = relationship("ClienteServico", back_populates="servico")
