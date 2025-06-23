import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = "http://localhost:8000/usuarios"

class UsuarioScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Usuários - SGS")

        tk.Label(root, text="ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1)

        tk.Label(root, text="Nome do Grupo:").grid(row=1, column=0)
        self.entry_nome_grupo = tk.Entry(root)
        self.entry_nome_grupo.grid(row=1, column=1)

        tk.Label(root, text="Login:").grid(row=2, column=0)
        self.entry_login = tk.Entry(root)
        self.entry_login.grid(row=2, column=1)

        tk.Label(root, text="Senha:").grid(row=3, column=0)
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.grid(row=3, column=1)

        tk.Button(root, text="Cadastrar", command=self.cadastrar).grid(row=4, column=0)
        tk.Button(root, text="Buscar", command=self.buscar).grid(row=4, column=1)
        tk.Button(root, text="Atualizar", command=self.atualizar).grid(row=5, column=0)
        tk.Button(root, text="Excluir", command=self.excluir).grid(row=5, column=1)
        tk.Button(root, text="Limpar", command=self.limpar).grid(row=6, column=0, columnspan=2)

    def get_data(self):
        return {
            "nome_grupo": self.entry_nome_grupo.get(),
            "login": self.entry_login.get(),
            "senha": self.entry_senha.get()
        }

    def preencher(self, data):
        self.entry_nome_grupo.delete(0, tk.END)
        self.entry_nome_grupo.insert(0, data.get("nome_grupo", ""))
        self.entry_login.delete(0, tk.END)
        self.entry_login.insert(0, data.get("login", ""))
        # Não preenche a senha por segurança

    def limpar(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nome_grupo.delete(0, tk.END)
        self.entry_login.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)

    def cadastrar(self):
        response = requests.post(BASE_URL + "/", json=self.get_data())
        messagebox.showinfo("Resultado", response.text)

    def buscar(self):
        id = self.entry_id.get()
        response = requests.get(BASE_URL + f"/{id}")
        if response.ok:
            self.preencher(response.json())
        else:
            messagebox.showerror("Erro", response.text)

    def atualizar(self):
        id = self.entry_id.get()
        response = requests.put(BASE_URL + f"/{id}", json=self.get_data())
        messagebox.showinfo("Resultado", response.text)

    def excluir(self):
        id = self.entry_id.get()
        response = requests.delete(BASE_URL + f"/{id}")
        messagebox.showinfo("Resultado", response.text)
