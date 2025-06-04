from pydantic import BaseModel
from typing import List, Optional

class UsuarioBase(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        orm_mode = True