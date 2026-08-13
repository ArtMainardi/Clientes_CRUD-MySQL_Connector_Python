import mysql.connector
from config import DB_CONFIG

conexao = None

def conectar():
    conexao = mysql.connector.connect(**DB_CONFIG)
    return conexao.cursor()

def criar_tabela():
    try:
        cursor = conectar()

        cursor.execute('''
            CREATE TABLE Clientes(
                id_usuario INT PRIMARY KEY AUTO_INCREMENT,
                NOME VARCHAR(100) NOT NULL,
                EMAIL VARCHAR(255) UNIQUE,
                TELEFONE CHAR(14) UNIQUE
            );
        ''')

        cursor.commit()
        print("Tabela 'Clientes' criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"ERRO: {e}")
    finally:
        if conexao.is_connected():
            conexao.close()