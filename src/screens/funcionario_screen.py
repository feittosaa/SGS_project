import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = "http://localhost:8000/funcionarios"

class FuncionarioScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Funcionários - SGS")

        tk.Label(root, text="ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1)

        tk.Label(root, text="Nome:").grid(row=1, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=1, column=1)

        tk.Label(root, text="Salário:").grid(row=2, column=0)
        self.entry_salario = tk.Entry(root)
        self.entry_salario.grid(row=2, column=1)

        tk.Label(root, text="ID Grupo:").grid(row=3, column=0)
        self.entry_id_grupo = tk.Entry(root)
        self.entry_id_grupo.grid(row=3, column=1)

        tk.Button(root, text="Cadastrar", command=self.cadastrar).grid(row=4, column=0)
        tk.Button(root, text="Buscar", command=self.buscar).grid(row=4, column=1)
        tk.Button(root, text="Atualizar", command=self.atualizar).grid(row=5, column=0)
        tk.Button(root, text="Excluir", command=self.excluir).grid(row=5, column=1)
        tk.Button(root, text="Limpar", command=self.limpar).grid(row=6, column=0, columnspan=2)

    def get_data(self):
        return {
            "nome": self.entry_nome.get(),
            "salario": float(self.entry_salario.get()),
            "id_grupo": int(self.entry_id_grupo.get())
        }

    def preencher(self, data):
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, data.get("nome", ""))
        self.entry_salario.delete(0, tk.END)
        self.entry_salario.insert(0, str(data.get("salario", "")))
        self.entry_id_grupo.delete(0, tk.END)
        self.entry_id_grupo.insert(0, str(data.get("id_grupo", "")))

    def limpar(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)
        self.entry_id_grupo.delete(0, tk.END)

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
