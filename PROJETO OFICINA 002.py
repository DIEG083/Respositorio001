from tkinter import *
import sqlite3
#reservado para inclusão de dados
conexao = sqlite3.connect('meu_banco.db')
cursor=conexao.cursor()
cursor.execute("CREATE table REGISTROS (cliente text,veiculo text, servico text, data text, HODOMETRO text )")
cursor.execute("INSERT into REGISTROS VALUES('jose','celta vermelho qff4823','troca de oleo')")
conexao.commit()
cursor.execute("SELECT * FROM REGISTROS")
print(cursor.fetchall())

janela1 = Tk()
janela1.title("REGISTRO DE SERVIÇOS")

#informações sobre o cliente:
texto_orientador = Label(janela1, text = ("Insira o nome do cliente"))
texto_orientador.grid(column=0,row=0)

texto_orientador2 = Label(janela1, text = ("Insira as informações do veículo "))
texto_orientador2.grid(column=0,row=2)

texto_orientador3 = Label(janela1, text = ("Informe o diagnóstico do veículo "))
texto_orientador3.grid(column=0,row=3 )
janela1.mainloop()