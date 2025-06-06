from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.usuario_schema import UsuarioCreate, UsuarioRead
from src.database.session import get_db
from src.services import usuario_service

router = APIRouter(tags=["Usuários"])

@router.post("/", response_model=UsuarioRead)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.criar_usuario(db, usuario)

@router.get("/", response_model=List[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioRead)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    item = usuario_service.obter_usuario(db, usuario_id)
    if not item:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return item

@router.put("/{usuario_id}", response_model=UsuarioRead)
def atualizar_usuario(usuario_id: int, dados: UsuarioCreate, db: Session = Depends(get_db)):
    item = usuario_service.atualizar_usuario(db, usuario_id, dados)
    if not item:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return item

@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    sucesso = usuario_service.deletar_usuario(db, usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return {"detail": "Usuario deletado com sucesso"}