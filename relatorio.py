import mysql.connector
import banco

def total_produtos():
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT nome, count(nome) FROM produtos group by id ORDER BY count(nome) asc")
        
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]}")
    except mysql.connector.Error as erro:
        print(f"ERRO: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def valor_total_estoque():
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT sum(preco) FROM produtos")
        
        for p in cursor.fetchall():
            print(f"{p[0]}")
    except mysql.connector.Error as erro:
        print(f"ERRO: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def produto_mais_caro():
    conexao = None
    try:
        conexao = banco.conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT nome FROM produtos order by preco desc limit 1")
        
        for p in cursor.fetchall():
            print(f"{p[0]}")
    except mysql.connector.Error as erro:
        print(f"ERRO: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()