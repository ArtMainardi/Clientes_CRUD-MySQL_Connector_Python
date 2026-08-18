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
    def __init__(self, nome, email, telefone):
        self.id = None
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

def listar():
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM Clientes;
        ''')
        lista = cursor.fetchall()

        if len(lista) != 0:
            for c in lista:
                print(f"ID: {c[0]}  |  Nome: {c[1]}  |  Email: {c[2]}  |  Telefone: {c[3]}")
        else:
            print("Nenhum dado encontrado!")
    except Exception as error:
        print("ERRO: " + error)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar(id):
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM Clientes WHERE id_cliente = %s
        ''', (id,))
        dado = cursor.fetchall()

        if len(dado) == 0:
            print("Nenhum dado com esse ID encontrado!")
        else:
            print(f"ID: {dado[0][0]}  |  Nome: {dado[0][1]}  |  Email: {dado[0][2]}  |  Telefone: {dado[0][3]}")
            return dado
    except Exception as error:
        print("ERRO: " + error)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()