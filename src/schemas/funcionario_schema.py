from pydantic import BaseModel

class FuncionarioBase(BaseModel):
    nome: str
    salario: float
    id_grupo: int

class FuncionarioCreate(FuncionarioBase):
    pass

class FuncionarioRead(FuncionarioBase):
    id: int

    class Config:
        orm_mode = True