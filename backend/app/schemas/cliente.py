from pydantic import BaseModel
from datetime import date
from .pet import Pet
from .contato import Contato
from .endereco import Endereco, EnderecoCreate, EnderecoUpdate
from app.models.models import PerfilUsuario

class ClienteBase(BaseModel):
    nome: str
    cpf: str


class ClienteUpdate(BaseModel):
    nome: str | None = None


class ClienteInDBBase(ClienteBase):
    id: int
    data_cadastro: date
    cpf: str

    class Config:
        from_attributes = True



class Cliente(ClienteInDBBase):
    pets: list[Pet] = []
    contatos: list[Contato] = []
    enderecos: list[Endereco] = []


class ClienteAdminResponse(Cliente):
    perfil: PerfilUsuario


class AdminClienteCreate(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    senha: str
    email: str
    telefone: str
    endereco: EnderecoCreate


class ClienteUpdate(BaseModel):
    """Schema para o cliente atualizar seus próprios dados."""
    nome: str | None = None
    sobrenome: str | None = None
    nova_senha: str | None = None
    email: str | None = None
    telefone: str | None = None
    endereco: EnderecoUpdate | None = None


class AdminClienteUpdate(BaseModel):
    """Schema para o administrador atualizar dados de um cliente."""
    nome: str | None = None
    sobrenome: str | None = None
    nova_senha: str | None = None
    email: str | None = None
    telefone: str | None = None
    endereco: EnderecoUpdate | None = None
