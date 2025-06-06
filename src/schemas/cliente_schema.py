from pydantic import BaseModel
from typing import Optional
from datetime import date

class ClienteBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    id_grupo: int
    cpf: Optional[str] = None
    data_aniversario: Optional[date] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteRead(ClienteBase):
    id: int

    class Config:
        orm_mode = True