from src.database.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    data_aniversario = Column(Date, nullable=False)
    telefone = Column(String(20), nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    grupo = relationship("Usuario", back_populates="clientes")
    compras = relationship("ClienteProduto", back_populates="cliente")
    servicos = relationship("ClienteServico", back_populates="cliente")
