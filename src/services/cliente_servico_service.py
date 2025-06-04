from sqlalchemy.orm import Session
from src.models.cliente_servico import ClienteServico
from src.schemas.cliente_servico_schema import ClienteServicoCreate

def criar_cliente_servico(db: Session, cliente_servico: ClienteServicoCreate):
    db_item = ClienteServico(**cliente_servico.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

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