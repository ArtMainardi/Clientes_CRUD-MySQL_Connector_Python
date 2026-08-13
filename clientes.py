import mysql.connector
import banco

banco.criar_tabela()

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