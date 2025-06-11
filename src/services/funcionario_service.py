from sqlalchemy.orm import Session
from src.models.funcionario import Funcionario
from src.schemas.funcionario_schema import FuncionarioCreate

def criar_funcionario(db: Session, funcionario: FuncionarioCreate):
    db_item = Funcionario(**funcionario.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def listar_funcionarios(db: Session):
    return db.query(Funcionario).all()

def obter_funcionario(db: Session, funcionario_id: int):
    return db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()

def atualizar_funcionario(db: Session, funcionario_id: int, dados: FuncionarioCreate):
    item = db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
    if not item:
        return None
    for key, value in dados.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def deletar_funcionario(db: Session, funcionario_id: int):
    item = db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True

def calcular_salario(funcionario: Funcionario, db: Session):
    if funcionario.tipo_salario == "fixo":
        return funcionario.salario
    elif funcionario.tipo_salario == "percentual_total":
        total = calcular_vendas_funcionario(funcionario.id, db)  #Implementar cálculo depois
        return total * funcionario.salario / 100
    elif funcionario.tipo_salario == "percentual_servico":
        total = calcular_servicos_funcionario(funcionario.id, db)  #Implementar cálculo depois
        return total * funcionario.salario / 100