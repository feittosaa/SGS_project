from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class ClienteServicoBase(BaseModel):
    id_cliente: Optional[int] = None
    id_funcionario: int
    id_servico: int
    valor: float
    observacoes: Optional[str]
    data_atendimento: datetime

class ClienteServicoCreate(BaseModel):
    id_cliente: Optional[int] = None  #Pode ser vendido para um cliente "anonimo", não cadastrado no sistema
    id_funcionario: int
    id_servico: int
    valor: float
    observacoes: Optional[str]
    data_atendimento: datetime

    @validator("valor")
    def valor_nao_negativo(cls, v):
        if v < 0:
            raise ValueError("O valor do serviço não pode ser negativo.")
        return v

class ClienteServicoRead(ClienteServicoBase):
    id: int

    class Config:
        orm_mode = True