# DB
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Functions
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS inscricao(nome TEXT,telefone TEXT,nascimento DATE,endereco TEXT,regiao TEXT,cep TEXT,email TEXT,facebook TEXT,instagram TEXT,sugestao TEXT)')

def add_data(nome,telefone,nascimento,endereco,regiao,cep,email,facebook,instagram,sugestao):
	c.execute('INSERT INTO inscricao(nome,telefone,nascimento,endereco,regiao,cep,email,facebook,instagram,sugestao) VALUES (?,?,?,?,?,?,?,?,?,?)',(nome,telefone,nascimento,endereco,regiao,cep,email,facebook,instagram,sugestao))
	conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	return data

def view_all_titles():
	c.execute('SELECT DISTINCT title FROM blogtable')
	data = c.fetchall()
	return data


def get_blog_by_title(title):
	c.execute('SELECT * FROM inscricao WHERE nome="{}"'.format(nome))
	data = c.fetchall()
	return data

def get_blog_by_author(author):
	c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
	data = c.fetchall()
	return data

def delete_data(title):
	c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
	conn.commit()