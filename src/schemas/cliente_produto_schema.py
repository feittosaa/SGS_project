from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class ClienteProdutoBase(BaseModel):
    id_cliente: Optional[int] = None
    id_funcionario: int
    id_produto: int
    valor_total: float
    quantidade: float
    data_venda: datetime

class ClienteProdutoCreate(BaseModel):
    id_cliente: Optional[int] = None  #Pode ser vendido para um cliente "anonimo", não cadastrado no sistema
    id_funcionario: int
    id_produto: int
    valor_total: float
    quantidade: float
    data_venda: Optional[datetime]

    @validator("quantidade")
    def quantidade_nao_negativa(cls, v):
        if v < 0:
            raise ValueError("A quantidade do produto não pode ser negativa.")
        return v


class ClienteProdutoRead(ClienteProdutoBase):
    id: int

    class Config:
        orm_mode = True
