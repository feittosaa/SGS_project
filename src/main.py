from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Funcionario(BaseModel):
    id: SERIAL
    nome: str
    salario: float
    id_grupo: int


Funcionarios = []

@app.get("/")
def root():
    return {"message": "Bem vindo!"}


@app.get("/Funcionarios", response_model=list[Funcionario])
def get_Funcionarios():
    if Funcionarios:
        return Funcionarios
    else:
        raise HTTPException(status_code=404, detail=f"Funcionário não encontrado")

@app.get("/Funcionarios/{Funcionario_id}", response_model=Funcionario)
def get_Funcionario(Funcionario_id: int) -> Funcionario:
    if Funcionario_id < len(Funcionarios):
        return Funcionarios[Funcionario_id]
    else:
        raise HTTPException(status_code=404, detail=f"Funcionário não encontrado")

@app.post("/Funcionarios")
def create_Funcionario(Funcionario: Funcionario):
    Funcionarios.append(Funcionario)
    return Funcionario
