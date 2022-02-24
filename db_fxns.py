# DB
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()




# Functions
def criar_tabela():
	c.execute('CREATE TABLE IF NOT EXISTS inscricoes (inscricao_id INTEGER PRIMARY KEY, nome TEXT,telefone TEXT,niver_dia INT,niver_mes TEXT,regiao TEXT,email TEXT,facebook TEXT,instagram TEXT,msg TEXT)')

def adicionar_dado(nome,telefone, niver_dia, niver_mes, regiao,email,facebook,instagram,msg):
	c.execute('INSERT INTO inscricoes (nome,telefone,niver_dia,niver_mes,regiao,email,facebook,instagram,msg) VALUES (?,?,?,?,?,?,?,?,?)',(nome,telefone,niver_dia,niver_mes,regiao,email,facebook,instagram,msg))
	conn.commit()

def ver_todas_incricoes():
	c.execute('SELECT * FROM inscricoes ORDER BY nome')
	data = c.fetchall()
	return data

def ver_todos_nomes():
	c.execute('SELECT DISTINCT nome FROM inscricoes ORDER BY nome')
	data = c.fetchall()
	return data


def pegar_inscricao_pelo_nome(nome):
	c.execute('SELECT * FROM inscricoes WHERE nome like "%{}%"'.format(nome))
	data = c.fetchall()
	return data

def pegar_inscricao_pelo_telefone(telefone):
	c.execute('SELECT * FROM inscricoes WHERE telefone like "%{}%"'.format(telefone))
	data = c.fetchall()
	return data

def apagar_dados(inscricao_id):
	c.execute('DELETE FROM inscricoes WHERE inscricao_id="{}"'.format(inscricao_id))
	conn.commit()