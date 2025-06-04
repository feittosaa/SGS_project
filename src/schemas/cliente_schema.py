from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    id_grupo: int

class ClienteCreate(ClienteBase):
    pass

class ClienteRead(ClienteBase):
    id: int

    class Config:
        orm_mode = True