from src.database.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    nome_grupo = Column(String(100), nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="grupo")
    produtos = relationship("Produto", back_populates="grupo")
    servicos = relationship("Servico", back_populates="grupo")
    clientes = relationship("Cliente", back_populates="grupo")
