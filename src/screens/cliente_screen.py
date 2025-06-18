import tkinter as tk
from tkinter import messagebox
import requests

BASE_URL = "http://localhost:8000/clientes"

class ClienteScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Clientes - SGS")

        # Labels e Entradas
        tk.Label(root, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_telefone = tk.Entry(root)
        self.entry_telefone.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="CPF:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(root, text="Data de Aniversário (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_data_aniversario = tk.Entry(root)
        self.entry_data_aniversario.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(root, text="ID Grupo:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_grupo = tk.Entry(root)
        self.entry_id_grupo.grid(row=5, column=1, padx=5, pady=5)

        # Botões
        tk.Button(root, text="Cadastrar", command=self.cadastrar_cliente).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(root, text="Buscar", command=self.buscar_cliente).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(root, text="Atualizar", command=self.atualizar_cliente).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(root, text="Excluir", command=self.excluir_cliente).grid(row=7, column=1, padx=5, pady=5)
        tk.Button(root, text="Limpar", command=self.limpar_campos).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    # Funções CRUD

    def cadastrar_cliente(self):
        data = self._get_form_data()
        response = requests.post(f"{BASE_URL}/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente:\n{response.text}")

    def buscar_cliente(self):
        cliente_id = self.entry_id.get()
        if not cliente_id:
            messagebox.showwarning("Aviso", "Informe o ID do cliente para buscar")
            return
        response = requests.get(f"{BASE_URL}/{cliente_id}")
        if response.status_code == 200:
            cliente = response.json()
            self._preencher_form(cliente)
        else:
            messagebox.showerror("Erro", f"Cliente não encontrado:\n{response.text}")

    def atualizar_cliente(self):
        cliente_id = self.entry_id.get()
        if not cliente_id:
            messagebox.showwarning("Aviso", "Informe o ID do cliente para atualizar")
            return
        data = self._get_form_data()
        response = requests.put(f"{BASE_URL}/{cliente_id}", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", f"Erro ao atualizar:\n{response.text}")

    def excluir_cliente(self):
        cliente_id = self.entry_id.get()
        if not cliente_id:
            messagebox.showwarning("Aviso", "Informe o ID do cliente para excluir")
            return
        response = requests.delete(f"{BASE_URL}/{cliente_id}")
        if response.status_code == 204:
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", f"Erro ao excluir:\n{response.text}")

    # Funções auxiliares

    def limpar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_data_aniversario.delete(0, tk.END)
        self.entry_id_grupo.delete(0, tk.END)

    def _get_form_data(self):
        data = {
            "nome": self.entry_nome.get(),
            "telefone": self.entry_telefone.get() or None,
            "cpf": self.entry_cpf.get() or None,
            "data_aniversario": self.entry_data_aniversario.get() or None,
            "id_grupo": int(self.entry_id_grupo.get()) if self.entry_id_grupo.get() else None
        }
        return data

    def _preencher_form(self, cliente):
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, cliente.get("nome", ""))

        self.entry_telefone.delete(0, tk.END)
        self.entry_telefone.insert(0, cliente.get("telefone") or "")

        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, cliente.get("cpf") or "")

        if cliente.get("data_aniversario"):
            self.entry_data_aniversario.delete(0, tk.END)
            self.entry_data_aniversario.insert(0, cliente.get("data_aniversario"))

        self.entry_id_grupo.delete(0, tk.END)
        self.entry_id_grupo.insert(0, cliente.get("id_grupo", ""))


# Main

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteScreen(root)
    root.mainloop()
