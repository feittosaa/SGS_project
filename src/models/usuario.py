from src.database.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    nome_grupo = Column(String(150), nullable=True)
    login = Column(String(150), nullable=False, unique=True)
    senha = Column(String(150), nullable=False)

    clientes = relationship("Cliente", back_populates="usuario")
    produtos = relationship("Produto", back_populates="usuario")
    servicos = relationship("Servico", back_populates="usuario")
    funcionarios = relationship("Funcionario", back_populates="usuario")

    def __init__(self, nome, nome_grupo, login, senha):
        self.nome = nome
        self.nome_grupo = nome_grupo
        self.login = login
        self.senha = senha