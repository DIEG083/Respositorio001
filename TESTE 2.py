import sqlite3
import tkinter as tk
from tkinter import ttk


# Função para conectar ao banco de dados e criar a tabela (se necessário)
def conectar_bd():
 conn = sqlite3.connect('meu_banco.db')  # Conecta ao banco de dados (ou cria se não existir)
 cursor = conn.cursor()
 # Cria uma tabela exemplo se não existir
 cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
 # Insere alguns dados de exemplo (opcional)
 cursor.execute('INSERT INTO pessoas (nome, idade) VALUES ("João", 25)')
 cursor.execute('INSERT INTO pessoas (nome, idade) VALUES ("Maria", 30)')
 cursor.execute('INSERT INTO pessoas (nome, idade) VALUES ("Ana", 22)')

 conn.commit()
 return conn


# Função para buscar os dados da tabela
def obter_dados():
 conn = conectar_bd()
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM pessoas")
 dados = cursor.fetchall()
 conn.close()
 return dados


# Função para exibir os dados em uma Treeview
def exibir_dados():
 dados = obter_dados()
 for row in dados:
  tree.insert('', tk.END, values=row)


# Criando a interface gráfica
janela = tk.Tk()
janela.title("Tabela de Dados")

# Configuração da tabela (Treeview)
tree = ttk.Treeview(janela, columns=("ID", "Nome", "Idade"), show="headings")
tree.heading("ID", text="+.ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")

tree.pack(fill=tk.BOTH, expand=True)

# Botão para exibir os dados
botao_exibir = tk.Button(janela, text="Exibir Dados", command=exibir_dados)
botao_exibir.pack()

# Executa a aplicação Tkinter
janela.mainloop()




