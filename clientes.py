import mysql.connector
import banco

banco.criar_tabela()

# Classe para um objeto 'cliente':
class cliente():
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

def criar(nome, email, telefone):
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            INSERT INTO Clientes (nome, email, telefone) VALUES (%s, %s, %s);
        ''', (nome, (email if email != "" else None), (telefone if telefone != "" else None)))

        conexao.commit()
        print("Cliente cadastrado com sucesso!!")
    except mysql.connector.Error as e:
        print("ERRO: ", e)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()