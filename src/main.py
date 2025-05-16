from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class FuncionarioInput(BaseModel):
    nome: str
    salario: float
    id_grupo: int

class Funcionario(FuncionarioInput):
    id: int

Funcionarios: list[Funcionario] = []
next_id = 1

@app.post("/funcionarios/", response_model=Funcionario)
def create_funcionario(func: FuncionarioInput):
    global next_id
    new_func = Funcionario(id=next_id, **func.dict())
    Funcionarios.append(new_func)
    next_id += 1
    return new_func

@app.get("/funcionarios/", response_model=list[Funcionario])
def list_funcionarios():
    return Funcionarios

@app.get("/funcionarios/{func_id}", response_model=Funcionario)
def get_funcionario(func_id: int):
    for f in Funcionarios:
        if f.id == func_id:
            return f
    raise HTTPException(status_code=404, detail="Funcionário não encontrado")