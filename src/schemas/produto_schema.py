from pydantic import BaseModel, validator

class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    uso_interno: bool
    valor: float
    quantidade: float
    id_grupo: int

class ProdutoCreate(ProdutoBase):
    nome: str
    categoria: str
    uso_interno: bool
    valor: float
    quantidade: float
    id_grupo: int

    @validator("valor")
    def valor_nao_negativo(cls, v):
        if v < 0:
            raise ValueError("O valor do produto não pode ser negativo.")
        return v

    @validator("quantidade")
    def quantidade_nao_negativa(cls, v):
        if v < 0:
            raise ValueError("A quantidade do produto não pode ser negativa.")
        return v

class ProdutoRead(ProdutoBase):
    id: int

    class Config:
        orm_mode = True