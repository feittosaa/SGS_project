@echo off
echo Iniciando FastAPI na porta 8000...
start cmd /k "uvicorn src.main:app --reload --port 8000"

timeout /t 3 > nul

echo Iniciando interface Tkinter...
start cmd /k "python src/screens/main_screen.py"