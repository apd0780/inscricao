# DB
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Functions
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS inscricao(nome TEXT,telefone TEXT,niver_dia INT,niver_mes TEXT,regiao TEXT,email TEXT,facebook TEXT,instagram TEXT,msg TEXT)')

def add_data(nome,telefone, niver_dia, niver_mes, regiao,email,facebook,instagram,msg):
	c.execute('INSERT INTO inscricao(nome,telefone,niver_dia,niver_mes,regiao,email,facebook,instagram,msg) VALUES (?,?,?,?,?,?,?,?,?)',(nome,telefone,niver_dia,niver_mes,regiao,email,facebook,instagram,msg))
	conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM inscricao')
	data = c.fetchall()
	return data

def view_all_titles():
	c.execute('SELECT DISTINCT nome FROM inscricao')
	data = c.fetchall()
	return data


def get_inscricao_by_nome(nome):
	c.execute('SELECT * FROM inscricao WHERE nome="{}"'.format(nome))
	data = c.fetchall()
	return data

def get_inscricao_by_telefone(telefone):
	c.execute('SELECT * FROM inscricao WHERE telefone="{}"'.format(telefone))
	data = c.fetchall()
	return data

def delete_data(title):
	c.execute('DELETE FROM inscricao WHERE nome="{}"'.format(nome))
	conn.commit()