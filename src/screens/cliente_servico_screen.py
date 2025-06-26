import tkinter as tk
from tkinter import messagebox, ttk
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000"

class ClienteServicoScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Atendimentos - Cliente Serviço")

        # Carregar opções
        self.clientes = self.get_opcoes("clientes")
        self.funcionarios = self.get_opcoes("funcionarios")
        self.servicos = self.get_opcoes("servicos")

        self.var_cliente = tk.StringVar()
        self.var_funcionario = tk.StringVar()
        self.var_servico = tk.StringVar()

        # Comboboxes e campos
        tk.Label(root, text="Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.select_cliente = ttk.Combobox(root, textvariable=self.var_cliente, values=list(self.clientes.keys()))
        self.select_cliente.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Funcionário:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.select_funcionario = ttk.Combobox(root, textvariable=self.var_funcionario, values=list(self.funcionarios.keys()))
        self.select_funcionario.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Serviço:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.select_servico = ttk.Combobox(root, textvariable=self.var_servico, values=list(self.servicos.keys()))
        self.select_servico.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Valor:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_valor = tk.Entry(root)
        self.entry_valor.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(root, text="Observações:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_observacoes = tk.Entry(root)
        self.entry_observacoes.grid(row=4, column=1, padx=5, pady=5)

        # Botões
        tk.Button(root, text="Registrar Atendimento", command=self.cadastrar).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(root, text="Limpar", command=self.limpar).grid(row=5, column=1, padx=5, pady=5)

    def get_opcoes(self, endpoint):
        try:
            response = requests.get(f"{BASE_URL}/{endpoint}")
            if response.status_code == 200:
                lista = response.json()
                return {item["nome"]: item["id"] for item in lista if "nome" in item}
            else:
                return {}
        except Exception as e:
            print(f"Erro ao buscar {endpoint}: {e}")
            return {}

    def get_data(self):
        return {
            "id_cliente": self.clientes.get(self.var_cliente.get()) if self.var_cliente.get() else None,
            "id_funcionario": self.funcionarios.get(self.var_funcionario.get()),
            "id_servico": self.servicos.get(self.var_servico.get()),
            "valor": float(self.entry_valor.get()),
            "observacoes": self.entry_observacoes.get() or None,
            "data_atendimento": datetime.utcnow().isoformat()
        }

    def cadastrar(self):
        data = self.get_data()
        response = requests.post(f"{BASE_URL}/clientes-servicos/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Atendimento registrado com sucesso!")
            self.limpar()
        else:
            messagebox.showerror("Erro", response.text)

    def limpar(self):
        self.var_cliente.set('')
        self.var_funcionario.set('')
        self.var_servico.set('')
        self.entry_valor.delete(0, tk.END)
        self.entry_observacoes.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteServicoScreen(root)
    root.mainloop()
