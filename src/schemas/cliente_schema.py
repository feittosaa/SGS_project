from pydantic import BaseModel, validator
import re
from typing import Optional
from datetime import date, datetime

class ClienteBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    id_grupo: int
    cpf: Optional[str] = None
    data_aniversario: Optional[date] = None

class ClienteCreate(BaseModel):
    nome: str
    telefone: Optional[str]
    cpf: Optional[str]
    data_aniversario: Optional[date]
    id_grupo: int

    @validator("cpf")
    def validar_cpf(cls, cpf):
        if cpf and not re.fullmatch(r"\d{11}", cpf):
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")  #Implementar cálculo depois
        return cpf

class ClienteRead(ClienteBase):
    id: int

    class Config:
        orm_mode = True

class ProdutoHistoricoSchema(BaseModel):
    id: int
    id_produto: int
    valor_total: float
    quantidade: int
    data_venda: datetime

    class Config:
        orm_mode = True

class ServicoHistoricoSchema(BaseModel):
    id: int
    id_servico: int
    valor: float
    data_atendimento: datetime
    observacoes: Optional[str]

    class Config:
        orm_mode = True

class ClienteHistoricoSchema(BaseModel):
    produtos: list[ProdutoHistoricoSchema]
    servicos: list[ServicoHistoricoSchema]
