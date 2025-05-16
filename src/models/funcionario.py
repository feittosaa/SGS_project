from sqlalchemy import Column, Integer, String, Float
from src.database import Base

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    salario = Column(Float, nullable=False)
