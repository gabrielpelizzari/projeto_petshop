"""
Testes para a API de pets.

Testa criação, listagem, atualização e exclusão de pets.
"""

from fastapi.testclient import TestClient


class TestPets:
    """Testes para gerenciamento de pets."""
    
    def test_listar_todos_pets_admin(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        raca_teste
    ):
        """
        Testa listagem de todos os pets (acesso admin).
        
        Admin deve conseguir ver todos os pets do sistema.
        """
        # Primeiro, cria um pet para ter dados
        pet_data = {
            "nome": "Rex",
            "data_nascimento": "2020-01-15",
            "raca_id": raca_teste.id
        }
        
        # Cria o pet
        client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=pet_data,
            headers=auth_headers_admin
        )
        
        # Lista todos os pets
        response = client.get("/api/pets/", headers=auth_headers_admin)
        
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        assert len(pets) >= 1
        assert pets[0]["nome"] == "Rex"
    

    def test_listar_pets_sem_permissao(self, client: TestClient, auth_headers_cliente):
        """
        Testa listagem de todos os pets sem permissão de admin.
        
        Cliente não deve conseguir ver todos os pets.
        """
        response = client.get("/api/pets/", headers=auth_headers_cliente)
        
        assert response.status_code == 403
    

    def test_criar_pet_sucesso(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente,
        dados_pet_valido
    ):
        """
        Testa criação de pet com dados válidos.
        
        Cliente deve conseguir criar pet para si mesmo.
        """
        cliente_id = usuario_cliente.cliente.id
        
        response = client.post(
            f"/api/clientes/{cliente_id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_cliente
        )
        
        assert response.status_code == 200
        pet = response.json()
        assert pet["nome"] == dados_pet_valido["nome"]
        assert pet["data_nascimento"] == dados_pet_valido["data_nascimento"]
        assert pet["raca_id"] == dados_pet_valido["raca_id"]
        assert pet["cliente_id"] == cliente_id
    

    def test_criar_pet_cliente_inexistente(
        self, 
        client: TestClient, 
        auth_headers_admin,
        dados_pet_valido
    ):
        """
        Testa criação de pet para cliente inexistente.
        
        Deve retornar erro 404.
        """
        cliente_id_inexistente = 99999
        
        response = client.post(
            f"/api/clientes/{cliente_id_inexistente}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin
        )
        
        assert response.status_code == 404
        assert "Cliente não encontrado" in response.json()["detail"]
    

    def test_criar_pet_raca_inexistente(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente
    ):
        """
        Testa criação de pet com raça inexistente.
        
        Deve retornar erro 404.
        """
        pet_data = {
            "nome": "Rex",
            "data_nascimento": "2020-01-15",
            "raca_id": 99999  # Raça inexistente
        }
        
        response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=pet_data,
            headers=auth_headers_cliente
        )
        
        assert response.status_code == 404
        assert "Raça não encontrada" in response.json()["detail"]
    

    def test_criar_pet_sem_permissao(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente,
        dados_pet_valido,
        db):
        """
        Testa criação de pet para outro cliente.
        
        Cliente não deve conseguir criar pet para outro cliente.
        """
        # Cria um segundo cliente para testar permissões
        from app.services import usuario_service
        from app.schemas.usuario import UsuarioCreate
        from app.models.models import PerfilUsuario
        
        segundo_cliente_data = UsuarioCreate(
            cpf="55566677788",
            nome="Outro Cliente",
            senha="senha123",
            perfil=PerfilUsuario.CLIENTE)
        segundo_usuario = usuario_service.create_usuario(db=db, usuario=segundo_cliente_data)
        
        # Tenta criar pet para outro cliente
        response = client.post(
            f"/api/clientes/{segundo_usuario.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_cliente)
        
        assert response.status_code == 403
        assert "Não tem permissão" in response.json()["detail"]
    

    def test_criar_pet_dados_obrigatorios_faltando(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente):
        """
        Testa criação de pet com dados obrigatórios faltando.
        
        Deve retornar erro 422.
        """
        pet_data_incompleto = {
            "nome": "Rex"
            # faltando data_nascimento e raca_id
        }
        
        response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=pet_data_incompleto,
            headers=auth_headers_cliente)
        
        assert response.status_code == 422
    

    def test_criar_pet_nome_vazio(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente,
        raca_teste):
        """
        Testa criação de pet com nome vazio.
        
        Deve retornar erro 422 com a nova validação.
        """
        pet_data = {
            "nome": "",  # Nome vazio
            "data_nascimento": "2020-01-15",
            "raca_id": raca_teste.id
        }
        
        response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=pet_data,
            headers=auth_headers_cliente
        )
        
        assert response.status_code == 422
        assert "Nome do pet não pode estar vazio" in str(response.json())
    

    def test_criar_pet_data_futura(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente,
        raca_teste):
        """
        Testa criação de pet com data de nascimento futura.
        
        Deve retornar erro de validação se houver validação de data.
        """
        pet_data = {
            "nome": "Rex",
            "data_nascimento": "2030-01-15",  # Data futura
            "raca_id": raca_teste.id
        }
        
        response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=pet_data,
            headers=auth_headers_cliente)
        
        assert response.status_code == 422
        assert "Data de nascimento não pode ser futura" in str(response.json())
    

    def test_listar_pets_do_cliente(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente,
        dados_pet_valido):
        """
        Testa listagem de pets de um cliente específico.
        
        Cliente deve conseguir ver seus próprios pets.
        """
        cliente_id = usuario_cliente.cliente.id
        
        # cria um pet
        client.post(
            f"/api/clientes/{cliente_id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_cliente)
        
        # Lista os pets do cliente
        response = client.get(
            f"/api/clientes/{cliente_id}/pets/",
            headers=auth_headers_cliente)
        
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        assert len(pets) >= 1
        assert pets[0]["nome"] == dados_pet_valido["nome"]
