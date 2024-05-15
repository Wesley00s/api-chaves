from fastapi import FastAPI

from database import connect_db
from functions import *
from models import RegistroChave, Usuario


app = FastAPI()


@app.post("/registrar-chave")
async def registrar_chave_controller(data: RegistroChave):
    conn = connect_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO registro_tb (mes, data, setor, nome, hora)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (data.mes, data.data, data.setor, data.nome, data.hora))
    conn.commit()

    cursor.close()
    conn.close()

    return data


@app.post("/login-usuario")
async def login_controller(data: Usuario):
    if login_usuario(data):
        return {"check": True, "message": "Login efetuado com sucesso"}
    else:
        return {"check": False, "message": "Combinação de senha e nome incorreta"}


@app.post("/registro-usuario")
async def registro_controller(data: Usuario):
    if registrar_usuario(data):
        return {"check": True, "message": "Registro feito com sucesso"}
    else:
        return {"check": False, "message": "Combinação não permitida"}


@app.put("/pegar-chave")
async def pegar_chave_controller(id: int):
    if pegar_chave(id):
        return {"check": True, "message": "Chave pegue com sucesso"}
    else:
        return {"check": False, "message": "Chave não pode ser pegue"}


@app.put("/devolver-chave")
async def devolver_chave_controller(id: int):
    if devolver_chave(id):
        return {"check": True, "message": "Chave devolvida com sucesso"}
    else:
        return {"check": False, "message": "Chave não pode ser devolvida"}


@app.post("/add-chave")
async def add_chave_controller():
    add_nova_chave()
    return {"check": True, "message": "Chave adicionada com sucesso"}


@app.get("/list-chaves")
async def list_chaves_controller():
    return listar_chaves()
