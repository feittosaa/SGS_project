@echo off
echo Iniciando FastAPI...
start cmd /k "uvicorn src.main:app --reload"

timeout /t 3 > nul

echo Iniciando interface Tkinter...
start cmd /k "python src/screens/cliente_screen.py"
