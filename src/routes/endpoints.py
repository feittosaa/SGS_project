from fastapi import APIRouter
from src.controllers import funcionario_controller

router = APIRouter()
router.include_router(funcionario_controller.router)
