import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, END
import requests
import re
from datetime import datetime

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

        tk.Label(root, text="CPF (000.000.000-00):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.grid(row=3, column=1, padx=5, pady=5)
        self.entry_cpf.bind("<KeyRelease>", self.formatar_cpf)

        tk.Label(root, text="Data Aniversário (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_data_aniversario = tk.Entry(root)
        self.entry_data_aniversario.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(root, text="ID Grupo:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_grupo = tk.Entry(root)
        self.entry_id_grupo.grid(row=5, column=1, padx=5, pady=5)

        # Botões principais
        tk.Button(root, text="Cadastrar", command=self.cadastrar_cliente).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(root, text="Buscar", command=self.buscar_cliente).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(root, text="Atualizar", command=self.atualizar_cliente).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(root, text="Excluir", command=self.excluir_cliente).grid(row=7, column=1, padx=5, pady=5)
        tk.Button(root, text="Limpar", command=self.limpar_campos).grid(row=8, column=0, padx=5, pady=5)
        tk.Button(root, text="Listar Todos", command=self.listar_todos).grid(row=8, column=1, padx=5, pady=5)
        tk.Button(root, text="Ver Histórico", command=self.ver_historico).grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    # Máscara CPF
    def formatar_cpf(self, event):
        texto = re.sub(r'\D', '', self.entry_cpf.get())[:11]
        formatado = ''
        if len(texto) > 0:
            formatado += texto[:3]
        if len(texto) > 3:
            formatado += '.' + texto[3:6]
        if len(texto) > 6:
            formatado += '.' + texto[6:9]
        if len(texto) > 9:
            formatado += '-' + texto[9:11]
        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, formatado)

    # Funções CRUD
    def cadastrar_cliente(self):
        data = self._get_form_data()
        if not self.validar_data(data["data_aniversario"]):
            return
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
        if not self.validar_data(data["data_aniversario"]):
            return
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
        if response.status_code == 200:
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", f"Erro ao excluir:\n{response.text}")

    # Listagem e histórico
    def listar_todos(self):
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            clientes = response.json()
            janela = Toplevel(self.root)
            janela.title("Lista de Clientes")
            text_area = Text(janela, wrap="word", width=80, height=20)
            scrollbar = Scrollbar(janela, command=text_area.yview)
            text_area.configure(yscrollcommand=scrollbar.set)
            text_area.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            for c in clientes:
                text_area.insert(END, f"{c}\n")
        else:
            messagebox.showerror("Erro", "Erro ao buscar clientes.")

    def ver_historico(self):
        cliente_id = self.entry_id.get()
        if not cliente_id:
            messagebox.showwarning("Aviso", "Informe o ID do cliente para ver o histórico")
            return
        response = requests.get(f"{BASE_URL}/{cliente_id}/historico")
        if response.status_code == 200:
            historico = response.json()
            janela = Toplevel(self.root)
            janela.title("Histórico do Cliente")
            text_area = Text(janela, wrap="word", width=100, height=20)
            scrollbar = Scrollbar(janela, command=text_area.yview)
            text_area.configure(yscrollcommand=scrollbar.set)
            text_area.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            text_area.insert(END, f"Produtos:\n")
            for p in historico["produtos"]:
                text_area.insert(END, f"{p}\n")
            text_area.insert(END, f"\nServiços:\n")
            for s in historico["servicos"]:
                text_area.insert(END, f"{s}\n")
        else:
            messagebox.showerror("Erro", "Erro ao buscar histórico.")

    # Auxiliares
    def limpar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_data_aniversario.delete(0, tk.END)
        self.entry_id_grupo.delete(0, tk.END)

    def _get_form_data(self):
        return {
            "nome": self.entry_nome.get(),
            "telefone": self.entry_telefone.get() or None,
            "cpf": re.sub(r'\D', '', self.entry_cpf.get()) or None,
            "data_aniversario": self.entry_data_aniversario.get() or None,
            "id_grupo": int(self.entry_id_grupo.get()) if self.entry_id_grupo.get() else None
        }

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

    def validar_data(self, data_str):
        if data_str:
            try:
                datetime.strptime(data_str, "%Y-%m-%d")
                return True
            except ValueError:
                messagebox.showerror("Erro", "Data inválida. Use o formato YYYY-MM-DD.")
                return False
        return True


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteScreen(root)
    root.mainloop()
