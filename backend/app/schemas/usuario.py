from pydantic import BaseModel
from app.models.models import PerfilUsuario

class UsuarioBase(BaseModel):
    cpf: str
    nome: str
    perfil: PerfilUsuario

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioUpdate(BaseModel):
    nome: str | None = None
    perfil: PerfilUsuario | None = None
    senha: str | None = None

class UsuarioInDBBase(UsuarioBase):
    class Config:
        from_attributes = True

class Usuario(UsuarioInDBBase):
    pass


class AdminUsuarioUpdate(BaseModel):
    nome: str | None = None
    nova_senha: str | None = None

class UsuarioUpdatePassword(BaseModel):
    senha_antiga: str
    nova_senha: str

class UsuarioInDB(UsuarioInDBBase):
    senha_hash: str
