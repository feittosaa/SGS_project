import tkinter as tk
from cliente_screen import ClienteScreen
from funcionario_screen import FuncionarioScreen
from produto_screen import ProdutoScreen
from servico_screen import ServicoScreen
from usuario_screen import UsuarioScreen
from cliente_produto_screen import ClienteProdutoScreen
from cliente_servico_screen import ClienteServicoScreen

def abrir_cliente():
    janela = tk.Toplevel(root)
    ClienteScreen(janela)

def abrir_funcionario():
    janela = tk.Toplevel(root)
    FuncionarioScreen(janela)

def abrir_produto():
    janela = tk.Toplevel(root)
    ProdutoScreen(janela)

def abrir_servico():
    janela = tk.Toplevel(root)
    ServicoScreen(janela)

def abrir_usuario():
    janela = tk.Toplevel(root)
    UsuarioScreen(janela)

def abrir_cliente_produto():
    janela = tk.Toplevel(root)
    ClienteProdutoScreen(janela)

def abrir_cliente_servico():
    janela = tk.Toplevel(root)
    ClienteServicoScreen(janela)

root = tk.Tk()
root.title("SGS - Sistema de Gerenciamento de Salões")

tk.Label(root, text="Selecione o módulo:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Vendas de Produtos", width=30, command=abrir_cliente_produto).pack(pady=5)
tk.Button(root, text="Vendas de Serviços", width=30, command=abrir_cliente_servico).pack(pady=5)
tk.Button(root, text="Clientes", width=30, command=abrir_cliente).pack(pady=5)
tk.Button(root, text="Funcionários", width=30, command=abrir_funcionario).pack(pady=5)
tk.Button(root, text="Produtos", width=30, command=abrir_produto).pack(pady=5)
tk.Button(root, text="Serviços", width=30, command=abrir_servico).pack(pady=5)
# tk.Button(root, text="Usuários", width=30, command=abrir_usuario).pack(pady=5)

root.mainloop()