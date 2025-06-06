from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    uso_interno: bool
    valor: float
    quantidade: float
    id_grupo: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoRead(ProdutoBase):
    id: int

    class Config:
        orm_mode = True