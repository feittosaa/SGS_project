from pydantic import BaseModel

class ServicoBase(BaseModel):
    nome: str
    categoria: str
    valor: float
    id_grupo: int

class ServicoCreate(ServicoBase):
    pass

class ServicoRead(ServicoBase):
    id: int

    class Config:
        orm_mode = True