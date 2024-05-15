import pymysql


def connect_db():
    return pymysql.connect(
        host="172.17.0.2",
        port=3306,
        user="root",
        password="senha",
        database="chaves_db"
    )


def create_table_chave():
    conn = connect_db()
    cursor = conn.cursor()

    # Cria a tabela de chaves se ela não existir
    create_query = """
    CREATE TABLE IF NOT EXISTS chave_tb (
        id INT AUTO_INCREMENT PRIMARY KEY,
        disponibilidade BOOLEAN
    )
    """
    cursor.execute(create_query)

    cursor.close()
    conn.close()


def create_table_registro():
    conn = connect_db()
    cursor = conn.cursor()

    # Cria a tabela de registros se ela não existir
    create_query = """
    CREATE TABLE IF NOT EXISTS registro_tb (
        id INT AUTO_INCREMENT PRIMARY KEY,
        mes VARCHAR(20),
        data VARCHAR(20),
        setor VARCHAR(50),
        nome VARCHAR(50),
        hora VARCHAR(10)
    )
    """
    cursor.execute(create_query)

    cursor.close()
    conn.close()


def create_table_user():
    conn = connect_db()
    cursor = conn.cursor()

    # Cria a tabela de usuários se ela não existir
    create_query = """
    CREATE TABLE IF NOT EXISTS usuario_tb (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50),
        senha VARCHAR(50)
    )
    """
    cursor.execute(create_query)

    cursor.close()
    conn.close()
