from sqlalchemy.orm import Session
from src.models.funcionario import Funcionario
from src.schemas.funcionario_schema import FuncionarioCreate, FuncionarioUpdate
from src.repositories.funcionario_repository import FuncionarioRepository

class FuncionarioService:
    def __init__(self, db: Session):
        self.repo = FuncionarioRepository(db)

    def listar(self):
        return self.repo.get_all()

    def buscar_por_id(self, id: int):
        return self.repo.get_by_id(id)

    def criar(self, data: FuncionarioCreate):
        novo = Funcionario(nome=data.nome, salario=data.salario)
        return self.repo.create(novo)

    def editar(self, id: int, data: FuncionarioUpdate):
        funcionario = self.repo.get_by_id(id)
        if not funcionario:
            return None
        return self.repo.update(funcionario, data.dict())

    def excluir(self, id: int):
        funcionario = self.repo.get_by_id(id)
        if not funcionario:
            return None
        self.repo.delete(funcionario)
        return funcionario
