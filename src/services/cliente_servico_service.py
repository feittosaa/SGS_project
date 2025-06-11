from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.cliente_servico import ClienteServico
from src.models.cliente import Cliente
from src.models.funcionario import Funcionario
from src.models.servico import Servico
from src.schemas.cliente_servico_schema import ClienteServicoCreate

def criar_cliente_servico(db: Session, cliente_servico: ClienteServicoCreate):

    if cliente_servico.id_cliente is not None:
        cliente = db.query(Cliente).filter(Cliente.id == cliente_servico.id_cliente).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if cliente_servico.id_funcionario is not None:
        funcionario = db.query(Funcionario).filter(Funcionario.id == cliente_servico.id_funcionario).first()
        if not funcionario:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    servico = db.query(Servico).filter(Servico.id == cliente_servico.id_servico).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    if cliente_servico.valor < 0:
        raise HTTPException(status_code=400, detail="O valor do serviço não pode ser negativo")

    db_item = ClienteServico(**cliente_servico.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def listar_clientes_servicos(db: Session):
    return db.query(ClienteServico).all()

def obter_cliente_servico(db: Session, cliente_servico_id: int):
    return db.query(ClienteServico).filter(ClienteServico.id == cliente_servico_id).first()

def atualizar_cliente_servico(db: Session, cliente_servico_id: int, dados: ClienteServicoCreate):
    item = db.query(ClienteServico).filter(ClienteServico.id == cliente_servico_id).first()
    if not item:
        return None
    for key, value in dados.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def deletar_cliente_servico(db: Session, cliente_servico_id: int):
    item = db.query(ClienteServico).filter(ClienteServico.id == cliente_servico_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True