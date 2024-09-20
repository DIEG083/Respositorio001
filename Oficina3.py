from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import ttk



# Função para criar a tabela
# con = sqlite3.connect('meu_banco.db')
# cur = con.cursor()
# cur.execute("""CREATE TABLE  SERVICOS (
#     id INTEGER PRIMARY KEY,
#     cliente TEXT,
#     veiculo TEXT,
#     servico TEXT,
#     data TEXT,
#     hodometro INTEGER
# )""")
# con.commit()
# con.close()

# FUNÇÃO DE CADASTRO
def cadastrar_servico():
    try:
        con = sqlite3.connect('meu_banco.db')
        cur = con.cursor()

        # Inserção de dados na tabela
        cur.execute("INSERT INTO SERVICOS (id, cliente, veiculo, servico, data, hodometro) VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        entrada1.get(),
                        entrada2.get(),
                        entrada3.get(),
                        entrada4.get(),
                        entrada5.get(),
                        entrada6.get()
                    ))

        con.commit()
        con.close()
        print("Serviço cadastrado com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao cadastrar serviço: {e}")

    entrada1.delete(0,'end')
    entrada2.delete(0, 'end')
    entrada3.delete(0, 'end')
    entrada4.delete(0, 'end')
    entrada5.delete(0, 'end')
    entrada6.delete(0, 'end')

def obter_dados():
    con = sqlite3.connect('meu_banco.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM SERVICOS")
    dados = cur.fetchall()
    con.commit()
    con.close()
    return dados

def exporta_clientes():
  dados = obter_dados()
  for row in dados:
    tree.insert('', tk.END, values=row)


janela2 = Tk()
janela2.title("HISTORICO DE SERVIÇOS ")
janela2.geometry('1200x200')

tree = ttk.Treeview(janela2, selectmode="browse",
                        column=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings')

tree.column("column1", width=200, minwidth=50, stretch=NO)
tree.heading("#1", text="ID")

tree.column("column2", width=200, minwidth=50, stretch=NO)
tree.heading("#2", text="CLIENTE")

tree.column("column3", width=200, minwidth=50, stretch=NO)
tree.heading("#3", text="VEICULO")

tree.column("column4", width=200, minwidth=50, stretch=NO)
tree.heading("#4", text="SERVIÇO")

tree.column("column5", width=200, minwidth=50, stretch=NO)
tree.heading("#5", text="DATA")

tree.column("column6", width=200, minwidth=50, stretch=NO)
tree.heading("#6", text="HODOMETRO")
tree.grid(row=0, column=0)

tree.pack(fill=tk.BOTH, expand=True)





# INTERFACE GRÁFICA
janela1 = Tk()
janela1.title("SERVIÇOS")
janela1.geometry('570x300')

# Labels
Label(janela1, text="INSIRA O NUMERO DO ORÇAMENTO (ID)").grid(column=0, row=1, padx=10, pady=10)
Label(janela1, text="INFORME O NOME DO CLIENTE").grid(column=0, row=2, padx=10, pady=10)
Label(janela1, text="INSIRA AS INFORMAÇÕES DO VEÍCULO").grid(column=0, row=3, pady=10, padx=10)
Label(janela1, text="DESCREVA O SERVIÇO REALIZADO").grid(column=0, row=4, padx=10, pady=10)
Label(janela1, text="DATA QUE FOI REALIZADO O SERVIÇO").grid(column=0, row=5, padx=10, pady=10)
Label(janela1, text="INFORME O HODÔMETRO ATUAL DO VEÍCULO (KM)").grid(column=0, row=6, pady=10, padx=10)

# Entradas
entrada1 = Entry(janela1, width=30)
entrada1.grid(column=1, row=1, padx=10, pady=10)

entrada2 = Entry(janela1, width=30)
entrada2.grid(column=1, row=2, padx=10, pady=10)

entrada3 = Entry(janela1, width=30)
entrada3.grid(column=1, row=3, pady=10, padx=10)

entrada4 = Entry(janela1, width=30)
entrada4.grid(column=1, row=4, padx=10, pady=10)

entrada5 = Entry(janela1, width=30)
entrada5.grid(column=1, row=5, padx=10, pady=10)

entrada6 = Entry(janela1, width=30)
entrada6.grid(column=1, row=6, pady=10, padx=10)


# Botão
botaocad = Button(janela1, text="CADASTRAR SERVIÇO", command=cadastrar_servico)
botaocad.grid(column=1, row=8, padx=10, pady=10, ipadx=60)

botaodb= Button(janela1, text = "VERIFICAR HISTÓRICO", command= exporta_clientes)
botaodb.grid(column=0,row=8, padx=10, pady=10,ipadx=60)

janela1.mainloop()
