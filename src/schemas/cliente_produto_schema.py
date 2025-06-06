from pydantic import BaseModel
from datetime import datetime

class ClienteProdutoBase(BaseModel):
    id_cliente: int
    id_funcionario: int
    id_produto: int
    valor_total: float
    quantidade: float
    data_venda: datetime

class ClienteProdutoCreate(ClienteProdutoBase):
    pass

class ClienteProdutoRead(ClienteProdutoBase):
    id: int

    class Config:
        orm_mode = True
