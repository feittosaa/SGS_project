import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL_PRODUTOS = "http://localhost:8000/clientes-produtos"
BASE_URL_SERVICOS = "http://localhost:8000/clientes-servicos"
BASE_URL_CLIENTES = "http://localhost:8000/clientes"
BASE_URL_FUNCIONARIOS = "http://localhost:8000/funcionarios"
BASE_URL_PRODUTOS_NOMES = "http://localhost:8000/produtos"
BASE_URL_SERVICOS_NOMES = "http://localhost:8000/servicos"

class HistoricoScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Histórico Geral - Vendas e Serviços")

        tk.Button(root, text="Carregar Histórico Geral", command=self.buscar_historico_geral).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Produtos
        tk.Label(root, text="Histórico de Produtos (Vendas)").grid(row=1, column=0, columnspan=2)
        self.tree_produtos = ttk.Treeview(root, columns=("id", "cliente", "funcionario", "produto", "qtd", "data", "valor"), show="headings")
        self.tree_produtos.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        for col, name in zip(self.tree_produtos["columns"], ["ID", "Cliente", "Funcionário", "Produto", "Qtd", "Data", "Valor (R$)"]):
            self.tree_produtos.heading(col, text=name)
            self.tree_produtos.column(col, width=120)

        # Serviços
        tk.Label(root, text="Histórico de Serviços (Atendimentos)").grid(row=3, column=0, columnspan=2)
        self.tree_servicos = ttk.Treeview(root, columns=("id", "cliente", "funcionario", "servico", "obs", "data", "valor"), show="headings")
        self.tree_servicos.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        for col, name in zip(self.tree_servicos["columns"], ["ID", "Cliente", "Funcionário", "Serviço", "Observações", "Data", "Valor (R$)"]):
            self.tree_servicos.heading(col, text=name)
            self.tree_servicos.column(col, width=120)

    def buscar_historico_geral(self):
        try:
            produtos = requests.get(BASE_URL_PRODUTOS).json()
            servicos = requests.get(BASE_URL_SERVICOS).json()
            clientes = {c["id"]: c["nome"] for c in requests.get(BASE_URL_CLIENTES).json()}
            funcionarios = {f["id"]: f["nome"] for f in requests.get(BASE_URL_FUNCIONARIOS).json()}
            nomes_produtos = {p["id"]: p["nome"] for p in requests.get(BASE_URL_PRODUTOS_NOMES).json()}
            nomes_servicos = {s["id"]: s["nome"] for s in requests.get(BASE_URL_SERVICOS_NOMES).json()}

            self.preencher_tabelas(produtos, servicos, clientes, funcionarios, nomes_produtos, nomes_servicos)

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar histórico:\n{e}")

    def preencher_tabelas(self, produtos, servicos, clientes, funcionarios, nomes_produtos, nomes_servicos):
        self.tree_produtos.delete(*self.tree_produtos.get_children())
        self.tree_servicos.delete(*self.tree_servicos.get_children())

        for venda in produtos:
            self.tree_produtos.insert("", tk.END, values=(
                venda["id"],
                clientes.get(venda.get("id_cliente")) or "-",
                funcionarios.get(venda["id_funcionario"], "Desconhecido"),
                nomes_produtos.get(venda["id_produto"], "Desconhecido"),
                venda["quantidade"],
                venda["data_venda"].split("T")[0],
                f'{venda["valor_total"]:.2f}'
            ))

        for servico in servicos:
            self.tree_servicos.insert("", tk.END, values=(
                servico["id"],
                clientes.get(servico.get("id_cliente")) or "-",
                funcionarios.get(servico["id_funcionario"], "Desconhecido"),
                nomes_servicos.get(servico["id_servico"], "Desconhecido"),
                servico.get("observacoes", ""),
                servico["data_atendimento"].split("T")[0],
                f'{servico["valor"]:.2f}'
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = HistoricoScreen(root)
    root.mainloop()
