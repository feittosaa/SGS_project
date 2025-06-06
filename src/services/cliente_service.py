from sqlalchemy.orm import Session
from src.models.cliente import Cliente
from src.schemas.cliente_schema import ClienteCreate

def criar_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def listar_clientes(db: Session):
    return db.query(Cliente).all()

def obter_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def atualizar_cliente(db: Session, cliente_id: int, dados: ClienteCreate):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        return None
    for key, value in dados.dict().items():
        setattr(cliente, key, value)
    db.commit()
    db.refresh(cliente)
    return cliente

def deletar_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        return False
    db.delete(cliente)
    db.commit()
    return True