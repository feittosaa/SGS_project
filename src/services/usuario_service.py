from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.schemas.usuario_schema import UsuarioCreate

def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_item = Usuario(**usuario.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def obter_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def atualizar_usuario(db: Session, usuario_id: int, dados: UsuarioCreate):
    item = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not item:
        return None
    for key, value in dados.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def deletar_usuario(db: Session, usuario_id: int):
    item = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True