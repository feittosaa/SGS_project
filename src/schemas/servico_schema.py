from pydantic import BaseModel, validator

class ServicoBase(BaseModel):
    nome: str
    categoria: str
    valor: float
    id_grupo: int

class ServicoCreate(BaseModel):
    nome: str
    categoria: str
    valor: float
    id_grupo: int

    @validator("valor")
    def valor_nao_negativo(cls, v):
        if v < 0:
            raise ValueError("O valor do serviço não pode ser negativo.")
        return v

class ServicoRead(ServicoBase):
    id: int

    class Config:
        orm_mode = True