from pydantic import BaseModel

class FuncionarioBase(BaseModel):
    nome: str
    salario: float

class FuncionarioCreate(FuncionarioBase):
    pass

class FuncionarioUpdate(FuncionarioBase):
    pass

class FuncionarioResponse(FuncionarioBase):
    id: int

    class Config:
        orm_mode = True
