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

def criar(cliente):
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            INSERT INTO Clientes (nome, email, telefone) VALUES (%s, %s, %s);
        ''', (cliente.nome, (cliente.email if cliente.email != "" else None), (cliente.telefone if cliente.telefone != "" else None)))

        conexao.commit()
        print("Cliente cadastrado com sucesso!!")
    except mysql.connector.Error as e:
        print("ERRO: ", e)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def atualizar(cliente):
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            UPDATE Clientes SET nome = %s, email = %s, telefone = %s WHERE id_cliente = %s;
        ''', (cliente.nome, (cliente.email if cliente.email != "" else None), (cliente.telefone if cliente.telefone != "" else None), cliente.id))

        conexao.commit()
        print("Cliente atualizado!!")
    except mysql.connector.Error as error:
        print("ERRO: ", error)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()