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
            CREATE TABLE IF NOT EXISTS Clientes(
                id_cliente INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(255) UNIQUE,
                telefone CHAR(14) UNIQUE
            );
        ''')

        conexao.commit()
        print("Tabela 'Clientes' criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"ERRO: {e}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()