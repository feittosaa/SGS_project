from src.database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    telefone = Column(String(20), nullable=True)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    cpf = Column(String(20), nullable=True)
    data_aniversario = Column(Date, nullable=True)

    usuario = relationship("Usuario", back_populates="clientes")
    produtos = relationship("ClienteProduto", back_populates="cliente", cascade="all, delete-orphan")
    servicos = relationship("ClienteServico", back_populates="cliente", cascade="all, delete-orphan")

    def __init__(self, nome, telefone, id_grupo, cpf=None, data_aniversario=None):
        self.nome = nome
        self.telefone = telefone
        self.id_grupo = id_grupo
        self.cpf = cpf
        self.data_aniversario = data_aniversario