"""
Configuração dos testes para o projeto PetShop.

Este arquivo configura:
- Banco de dados de teste em memória
- Cliente de teste para fazer requisições HTTP
- Fixtures para criar dados de teste
- Autenticação para testes
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from main import app
from app.core.database import get_db
from app.models.models import Base
from app.core.security import create_access_token
from app.services import usuario_service, raca_service
from app.schemas.usuario import UsuarioCreate
from app.schemas.raca import RacaCreate
from app.models.models import PerfilUsuario


# Banco de dados de teste em memória (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """
    Cria um banco de dados de teste para cada teste.
    
    Cada teste roda com um banco limpo e isolado.
    """
    # Cria as tabelas
    Base.metadata.create_all(bind=engine)
    
    # Cria a sessão
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Remove as tabelas após o teste
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """
    Cliente de teste para fazer requisições HTTP.
    
    Substitui a dependência do banco de dados pela sessão de teste.
    """
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    # Limpa as dependências após o teste
    app.dependency_overrides.clear()


@pytest.fixture
def usuario_admin(db):
    """
    Cria um usuário administrador para testes.
    
    Returns:
        Usuario: Usuário administrador criado
    """
    usuario_data = UsuarioCreate(
        cpf="12345678901",
        nome="Admin Teste",
        senha="senha123",
        perfil=PerfilUsuario.ADMIN
    )
    return usuario_service.create_usuario(db=db, usuario=usuario_data)


@pytest.fixture
def usuario_cliente(db):
    """
    Cria um usuário cliente para testes.
    
    Returns:
        Usuario: Usuário cliente criado
    """
    usuario_data = UsuarioCreate(
        cpf="98765432100",
        nome="Cliente Teste",
        senha="senha123",
        perfil=PerfilUsuario.CLIENTE
    )
    return usuario_service.create_usuario(db=db, usuario=usuario_data)


@pytest.fixture
def token_admin(usuario_admin):
    """
    Gera um token de acesso para o usuário administrador.
    
    Returns:
        str: Token de acesso válido
    """
    return create_access_token(subject=usuario_admin.cpf)


@pytest.fixture
def token_cliente(usuario_cliente):
    """
    Gera um token de acesso para o usuário cliente.
    
    Returns:
        str: Token de acesso válido
    """
    return create_access_token(subject=usuario_cliente.cpf)


@pytest.fixture
def auth_headers_admin(token_admin):
    """
    Headers de autenticação para administrador.
    
    Returns:
        dict: Headers com token de autorização
    """
    return {"Authorization": f"Bearer {token_admin}"}


@pytest.fixture
def auth_headers_cliente(token_cliente):
    """
    Headers de autenticação para cliente.
    
    Returns:
        dict: Headers com token de autorização
    """
    return {"Authorization": f"Bearer {token_cliente}"}


@pytest.fixture
def raca_teste(db):
    """
    Cria uma raça de teste.
    
    Returns:
        Raca: Raça criada para testes
    """
    raca_data = RacaCreate(nome="Labrador")
    return raca_service.create_raca(db=db, raca=raca_data)


# Dados de exemplo para testes
@pytest.fixture
def dados_cadastro_valido():
    """
    Dados válidos para teste de cadastro.
    
    Returns:
        dict: Dados de cadastro válidos
    """
    return {
        "nome": "João",
        "sobrenome": "Silva",
        "cpf": "12345678901",
        "senha": "senha123",
        "email": "joao@teste.com",
        "telefone": "11999999999",
        "endereco": {
            "logradouro": "Rua Teste, 123",
            "cidade": "São Paulo",
            "bairro": "Centro",
            "complemento": "Apto 101",
            "tag": "Principal"
        }
    }


@pytest.fixture
def dados_pet_valido(raca_teste):
    """
    Dados válidos para teste de pet.
    
    Returns:
        dict: Dados de pet válidos
    """
    return {
        "nome": "Rex",
        "data_nascimento": "2020-01-15",
        "raca_id": raca_teste.id
    }


@pytest.fixture
def dados_atendimento_valido():
    """
    Dados válidos para teste de atendimento.
    
    Returns:
        dict: Dados de atendimento válidos
    """
    return {
        "descricao": "Consulta de rotina",
        "valor": 150.00,
        "data": "2024-01-15"
    }
