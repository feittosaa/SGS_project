# SGS - Sistema de Gerenciamento de Salões

Este projeto é um sistema de gerenciamento de salões de beleza desenvolvido em **FastAPI** como parte da disciplina **PAV - Programação em Ambiente Visual** na faculdade.

O objetivo do projeto é fornecer uma API simples e funcional para gerenciar clientes, serviços e funcionários de salões de beleza.

---

## Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## Como Rodar o Projeto

1. Clone o repositório:
  ```bash
  git clone https://github.com/seu-usuario/SGS.git
  cd SGS

2. Crie um ambiente virtual:
  python -m venv venv
  source venv/bin/activate  # ou venv\Scripts\activate no Windows

3. Instale as dependências:
  pip install -r requirements.txt

4. Inicie o servidor:
  uvicorn app.main:app --reload

5. Acesse no navegador:
  API: http://localhost:8000/
  Documentação Swagger: http://localhost:8000/docs

---

## Menções e Fontes de Estudo
Aqui estão algumas fontes utilizadas para aprendizado:

Documentação oficial do FastAPI:
https://fastapi.tiangolo.com/

Python FastAPI Tutorial: Build a REST API in 15 Minutes - pixegami
(Vídeo em inglês, porém possui legendas em português)
https://www.youtube.com/watch?v=iWS9ogMPOI0
