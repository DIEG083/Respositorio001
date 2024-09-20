from tkinter import *
import sqlite3
import pandas

#BANCO DE DADOS (INSERÇÃO DOS DADOS)
conexao = sqlite3.connect('meu_banco.db')
cursor=conexao.cursor()

#Criando a tabela:
#cursor.execute("""CREATE TABLE  SERVICOS (
 #    id integer,
   # cliente text,
   # veiculo text,
   # servico text,
   # data text,
   # hodometro integer
   #  )""")

#FUNCOES
conexao.commit()

conexao.close()

def cadastrar_servico():
    conexao = sqlite3.connect('meu_banco.db')
    cursor=conexao.cursor()


    cursor.execute("INSERT INTO ORÇAMENTOS VALUES (:id,:cliente,:veiculo,:servico,:data,:hodometro)",
                 {
                   'id': entrada1.get(),
                   'cliente': entrada2.get(),
                   'veiculo': entrada3.get(),
                   'servico': entrada4.get(),
                   'data': entrada5.get(),
                   'hodometro': entrada6.get()
                })
    conexao.commit()
    conexao.close()
#cursor.execute("SELECT * FROM ORÇAMENTOS")
#print(cursor.fetchall())



def verficar_db():
  pass

#INTERFACE GRAFICA DO PROJETO



janela1 = Tk( )
janela1.title("REGISTRO DE SERVIÇOS")
janela1.geometry('570x300')

#informações sobre o cliente:
texto_orientador = Label(janela1, text = ("INSIRA O NUMERO DO ORÇAMENTO (ID) "))
texto_orientador.grid(column=0,row=1, padx=10, pady=10)

texto_orientador2 = Label(janela1, text = ("INFORME O NOME DO CLIENTE"))
texto_orientador2.grid(column=0,row=2, padx=10,pady=10)

texto_orientador3 = Label(janela1, text = ("INSIRA AS INFORMAÇÕES DO VEICULO"))
texto_orientador3.grid(column=0,row=3,pady=10,padx=10)

texto_orientador4 = Label(janela1, text = ("DESCREVA O SERVIÇO REALIZADO"))
texto_orientador4.grid(column=0,row=4, padx=10, pady=10)

texto_orientador5 = Label(janela1, text = ("DATA QUE FOI REALIZADO O SERVIÇO"))
texto_orientador5.grid(column=0,row=5, padx=10,pady=10)

texto_orientador6 = Label(janela1, text = ("INFORME O HODOMETRO ATUAL DO VEICULO (KM) "))
texto_orientador6.grid(column=0,row=6,pady=10,padx=10)





#ENTRADAS

entrada1= Entry(janela1,width=30)
entrada1.grid(column=1,row=1, padx=10, pady=10)

entrada2 = Entry(janela1,width=30)
entrada2.grid(column=1,row=2, padx=10,pady=10)

entrada3 = Entry(janela1,width=30)
entrada3.grid(column=1,row=3,pady=10,padx=10)

entrada4 = Entry(janela1,width=30)
entrada4.grid(column=1,row=4, padx=10, pady=10)

entrada5 = Entry(janela1,width=30)
entrada5.grid(column=1,row=5, padx=10,pady=10)

entrada6 = Entry(janela1,width=30)
entrada6.grid(column=1,row=6,pady=10,padx=10)

#BOTOES

botaocad = Button(text = "CADASTRAR SERVIÇO", command= cadastrar_servico)
botaocad.grid(column=1,row=8, padx=10, pady=10,ipadx=60)

botaodb= Button(janela1, text = "VERIFICAR HISTÓRICO", command= verficar_db)
botaodb.grid(column=0,row=8, padx=10, pady=10,ipadx=60)



janela1.mainloop()
