import mysql.connector
from config import DB_CONFIG

def conectar():
    conexao = mysql.connector.connect(**DB_CONFIG)
    return conexao

def criar_tabela():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE Clientes(
                id_usuario INT PRIMARY KEY AUTO_INCREMENT,
                NOME VARCHAR(100) NOT NULL,
                EMAIL VARCHAR(255) UNIQUE,
                TELEFONE CHAR(14) UNIQUE
            );
        ''')

        conexao.commit()
        print("Tabela 'Clientes' criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"ERRO: {e}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()