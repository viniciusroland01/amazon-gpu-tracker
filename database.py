import sqlite3

BANCO = "produtos.db"

def criar_tabela():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_do_produto TEXT NOT NULL,
        preco_atual REAL NOT NULL,
        link_oferta TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def inserir_produto(nome,preco,link):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome_do_produto, preco_atual,link_oferta)
    VALUES (?,?,?)       
    """, (nome,preco,link) )

    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conexao.close()
    return produtos