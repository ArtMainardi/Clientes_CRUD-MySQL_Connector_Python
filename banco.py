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

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100)  NOT NULL,
                preco DECIMAL(10,2) NOT NULL,
                quantidade INT,
                categoria VARCHAR(50)
            )
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"ERRO: {e}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()