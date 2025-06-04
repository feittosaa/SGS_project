from src.database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    telefone = Column(String(20), nullable=False)
    id_grupo = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="clientes")
    produtos = relationship("ClienteProduto", back_populates="cliente")
    servicos = relationship("ClienteServico", back_populates="cliente")

    def __init__(self, nome, telefone, id_grupo):
        self.nome = nome
        self.telefone = telefone
        self.id_grupo = id_grupo