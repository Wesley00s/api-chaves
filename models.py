from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    senha: str


class RegistroChave(BaseModel):
    mes: str
    data: str
    setor: str
    nome: str
    hora: str
