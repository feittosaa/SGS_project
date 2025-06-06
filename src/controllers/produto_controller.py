from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.produto_schema import ProdutoCreate, ProdutoRead
from src.database.session import get_db
from src.services import produto_service

router = APIRouter(tags=["Produtos"])

@router.post("/", response_model=ProdutoRead)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return produto_service.criar_produto(db, produto)

@router.get("/", response_model=List[ProdutoRead])
def listar_produtos(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)

@router.get("/{produto_id}", response_model=ProdutoRead)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    item = produto_service.obter_produto(db, produto_id)
    if not item:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return item

@router.put("/{produto_id}", response_model=ProdutoRead)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db: Session = Depends(get_db)):
    item = produto_service.atualizar_produto(db, produto_id, dados)
    if not item:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return item

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    sucesso = produto_service.deletar_produto(db, produto_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}