from sqlalchemy.orm import Session
from src.models.servico import Servico
from src.schemas.servico_schema import ServicoCreate

def criar_servico(db: Session, servico: ServicoCreate):
    db_item = Servico(**servico.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def listar_servicos(db: Session):
    return db.query(Servico).all()

def obter_servico(db: Session, servico_id: int):
    return db.query(Servico).filter(Servico.id == servico_id).first()

def atualizar_servico(db: Session, servico_id: int, dados: ServicoCreate):
    item = db.query(Servico).filter(Servico.id == servico_id).first()
    if not item:
        return None
    for key, value in dados.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def deletar_servico(db: Session, servico_id: int):
    item = db.query(Servico).filter(Servico.id == servico_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True