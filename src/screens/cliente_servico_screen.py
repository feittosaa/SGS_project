import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000/clientes-servicos"

class ClienteServicoScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Atendimentos - Cliente Serviço")

        # Labels e Entradas
        tk.Label(root, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="ID Cliente:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_cliente = tk.Entry(root)
        self.entry_id_cliente.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="ID Funcionário:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_funcionario = tk.Entry(root)
        self.entry_id_funcionario.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="ID Serviço:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_servico = tk.Entry(root)
        self.entry_id_servico.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(root, text="Valor:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_valor = tk.Entry(root)
        self.entry_valor.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(root, text="Observações:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_observacoes = tk.Entry(root)
        self.entry_observacoes.grid(row=5, column=1, padx=5, pady=5)

        # Botões
        tk.Button(root, text="Registrar Atendimento", command=self.cadastrar).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(root, text="Buscar", command=self.buscar).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(root, text="Atualizar", command=self.atualizar).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(root, text="Excluir", command=self.excluir).grid(row=7, column=1, padx=5, pady=5)
        tk.Button(root, text="Limpar", command=self.limpar).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def get_data(self):
        return {
            "id_cliente": int(self.entry_id_cliente.get()) if self.entry_id_cliente.get() else None,
            "id_funcionario": int(self.entry_id_funcionario.get()),
            "id_servico": int(self.entry_id_servico.get()),
            "valor": float(self.entry_valor.get()),
            "observacoes": self.entry_observacoes.get() or None,
            "data_atendimento": datetime.utcnow().isoformat()
        }

    def cadastrar(self):
        response = requests.post(f"{BASE_URL}/", json=self.get_data())
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Atendimento registrado!")
            self.limpar()
        else:
            messagebox.showerror("Erro", response.text)

    def buscar(self):
        item_id = self.entry_id.get()
        if not item_id:
            messagebox.showwarning("Aviso", "Informe o ID")
            return
        response = requests.get(f"{BASE_URL}/{item_id}")
        if response.status_code == 200:
            item = response.json()
            self.entry_id_cliente.delete(0, tk.END)
            self.entry_id_cliente.insert(0, item.get("id_cliente") or "")
            self.entry_id_funcionario.delete(0, tk.END)
            self.entry_id_funcionario.insert(0, item["id_funcionario"])
            self.entry_id_servico.delete(0, tk.END)
            self.entry_id_servico.insert(0, item["id_servico"])
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.insert(0, item["valor"])
            self.entry_observacoes.delete(0, tk.END)
            self.entry_observacoes.insert(0, item.get("observacoes") or "")
        else:
            messagebox.showerror("Erro", response.text)

    def atualizar(self):
        item_id = self.entry_id.get()
        if not item_id:
            messagebox.showwarning("Aviso", "Informe o ID para atualizar")
            return
        response = requests.put(f"{BASE_URL}/{item_id}", json=self.get_data())
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Atendimento atualizado!")
        else:
            messagebox.showerror("Erro", response.text)

    def excluir(self):
        item_id = self.entry_id.get()
        if not item_id:
            messagebox.showwarning("Aviso", "Informe o ID para excluir")
            return
        response = requests.delete(f"{BASE_URL}/{item_id}")
        if response.status_code == 204:
            messagebox.showinfo("Sucesso", "Registro excluído!")
            self.limpar()
        else:
            messagebox.showerror("Erro", response.text)

    def limpar(self):
        self.entry_id.delete(0, tk.END)
        self.entry_id_cliente.delete(0, tk.END)
        self.entry_id_funcionario.delete(0, tk.END)
        self.entry_id_servico.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_observacoes.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteServicoScreen(root)
    root.mainloop()