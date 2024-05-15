from models import RegistroChave, Usuario
import pymysql


def add_registro(data: RegistroChave):
    conn = pymysql.connect(
        host="172.17.0.2",
        port=3306,
        user="root",
        password="senha",
        database="chaves_db"
    )

    cursor = conn.cursor()

    # Monta a query SQL para inserir o registro na tabela
    insert_query = """
    INSERT INTO registro_tb (mes, data, setor, nome, hora)
    VALUES (%s, %s, %s, %s, %s)
    """

    # Executa a query SQL com os dados fornecidos
    cursor.execute(insert_query, (data.mes, data.data, data.setor, data.nome, data.hora))

    # Faz commit da transação
    conn.commit()

    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()


def registrar_usuario(data: Usuario):
    conn = pymysql.connect(
        host="172.17.0.2",
        port=3306,
        user="root",
        password="senha",
        database="chaves_db"
    )

    cursor = conn.cursor()

    # Monta a query SQL para verificar se o usuário já existe na tabela
    check_query = """
    SELECT * FROM usuario_tb
    WHERE nome = %s AND senha = %s
    """

    # Executa a query SQL para verificar se o usuário já existe
    cursor.execute(check_query, (data.nome, data.senha))

    # Obtém o resultado da consulta
    existing_user = cursor.fetchone()

    # Verifica se o usuário já existe na tabela
    if existing_user:
        # Se o usuário já existe, retorna False
        return False
    else:
        # Se o usuário não existe, executa a inserção na tabela
        insert_query = """
        INSERT INTO usuario_tb (nome, senha)
        VALUES (%s, %s)
        """

        # Executa a query SQL para inserir o usuário na tabela
        cursor.execute(insert_query, (data.nome, data.senha))

        # Faz commit da transação
        conn.commit()

        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()

        # Retorna True para indicar que o usuário foi registrado com sucesso
        return True


def login_usuario(data: Usuario):
    conn = pymysql.connect(
        host="172.17.0.2",
        port=3306,
        user="root",
        password="senha",
        database="chaves_db"
    )

    cursor = conn.cursor()

    # Monta a query SQL para verificar o usuário na tabela através da senha
    verify_query = """
    SELECT * FROM usuario_tb
    WHERE nome = %s AND senha = %s
    """

    cursor.execute(verify_query, (data.nome, data.senha))

    user = cursor.fetchone()

    # Verifica se o usuário foi encontrado e se a senha está correta
    if user:
        # Usuário encontrado, retorna True (autenticado)
        return True
    else:
        # Usuário não encontrado ou senha incorreta, retorna False (não autenticado)
        return False


def pegar_chave(id: int):
    try:
        conn = pymysql.connect(
            host="172.17.0.2",
            port=3306,
            user="root",
            password="senha",
            database="chaves_db"
        )

        cursor = conn.cursor()

        # Verifica se a chave está disponível
        check_query = """
        SELECT disponibilidade
        FROM chave_tb
        WHERE id = %s
        """
        cursor.execute(check_query, (id,))
        disponibilidade = cursor.fetchone()

        if disponibilidade and disponibilidade[0]:  # Verifica se a chave está disponível
            # Atualiza o status da chave para indisponível
            put_query = """
            UPDATE chave_tb
            SET disponibilidade = FALSE
            WHERE id = %s
            """
            cursor.execute(put_query, (id,))
            conn.commit()

            cursor.close()
            conn.close()

            return True
        else:
            print("A chave não está disponível para ser pega.")
            return False
    except Exception as e:
        print("Erro ao pegar chave:", e)
        return False


def devolver_chave(id: int):
    try:
        conn = pymysql.connect(
            host="172.17.0.2",
            port=3306,
            user="root",
            password="senha",
            database="chaves_db"
        )

        cursor = conn.cursor()

        # Verifica se a chave está emprestada
        check_query = """
        SELECT disponibilidade
        FROM chave_tb
        WHERE id = %s
        """
        cursor.execute(check_query, (id,))
        disponibilidade = cursor.fetchone()

        if disponibilidade and not disponibilidade[0]:  # Verifica se a chave está emprestada
            # Atualiza o status da chave para disponível
            return_query = """
            UPDATE chave_tb
            SET disponibilidade = TRUE
            WHERE id = %s
            """
            cursor.execute(return_query, (id,))
            conn.commit()

            cursor.close()
            conn.close()

            return True
        else:
            print("A chave já está disponível.")
            return False
    except Exception as e:
        print("Erro ao devolver chave:", e)
        return False


def add_nova_chave():
    conn = pymysql.connect(
        host="172.17.0.2",
        port=3306,
        user="root",
        password="senha",
        database="chaves_db"
    )

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO chave_tb (disponibilidade)
    VALUES (TRUE)
    """

    cursor.execute(insert_query)
    conn.commit()

    cursor.close()
    conn.close()


def listar_chaves():
    conn = pymysql.connect(
        host="172.17.0.2",
        port=3306,
        user="root",
        password="senha",
        database="chaves_db"
    )

    cursor = conn.cursor()

    select_query = """
           SELECT *
           FROM chave_tb
           """

    cursor.execute(select_query)
    chaves = cursor.fetchall()

    cursor.close()
    conn.close()

    return chaves
