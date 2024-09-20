import sqlite3

conexao = sqlite3.connect('meu_banco.db')
try:
 cursor = conexao.cursor()
 cursor.execute('DELETE from SERVICOS where ID = 4 ')
 conexao.commit()
 conexao.close()
 print('Os dados foram exluídos com sucesso')

except sqlite3.Error as erro:
 print('Falha ao tentar excluir')