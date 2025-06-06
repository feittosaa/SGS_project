from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClienteServicoBase(BaseModel):
    id_cliente: int
    id_funcionario: int
    id_servico: int
    valor: float
    observacoes: Optional[str]
    data_atendimento: datetime

class ClienteServicoCreate(ClienteServicoBase):
    pass

class ClienteServicoRead(ClienteServicoBase):
    id: int

    class Config:
        orm_mode = True