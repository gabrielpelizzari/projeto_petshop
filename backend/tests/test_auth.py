"""
Testes para a API de autenticação.

Testa os endpoints de login e validação de tokens.
"""

from fastapi.testclient import TestClient


class TestAuth:
    """Testes para autenticação."""
    
    def test_login_sucesso(self, client: TestClient, usuario_admin):
        """
        Testa login com credenciais válidas.
        
        Deve retornar token de acesso válido.
        """
        # Dados de login
        login_data = {
            "username": usuario_admin.cpf,
            "password": "senha123"
        }
        
        # Faz a requisição de login
        response = client.post("/api/login", data=login_data)
        
        # Verifica se o login foi bem-sucedido
        assert response.status_code == 200
        
        # Verifica se retornou o token
        data = response.json()
        assert "access_token" in data
        assert "token_type" in data
        assert data["token_type"] == "bearer"
        assert len(data["access_token"]) > 0
    

    def test_login_cpf_invalido(self, client: TestClient):
        """
        Testa login com CPF inválido.
        
        Deve retornar erro 401.
        """
        login_data = {
            "username": "00000000000",
            "password": "senha123"
        }
        
        response = client.post("/api/login", data=login_data)
        
        assert response.status_code == 401
        assert "CPF ou senha incorretos" in response.json()["detail"]
    

    def test_login_senha_invalida(self, client: TestClient, usuario_admin):
        """
        Testa login com senha inválida.
        
        Deve retornar erro 401.
        """
        login_data = {
            "username": usuario_admin.cpf,
            "password": "senha_errada"
        }
        
        response = client.post("/api/login", data=login_data)
        
        assert response.status_code == 401
        assert "CPF ou senha incorretos" in response.json()["detail"]
    

    def test_login_dados_vazios(self, client: TestClient):
        """
        Testa login com dados vazios.
        
        OAuth2 retorna 401 para credenciais vazias.
        """
        login_data = {
            "username": "",
            "password": ""
        }
        
        response = client.post("/api/login", data=login_data)
        
        assert response.status_code == 401
    

    def test_acesso_endpoint_protegido_com_token_valido(
        self, 
        client: TestClient, 
        auth_headers_admin
    ):
        """
        Testa acesso a endpoint protegido com token válido.
        
        Deve permitir acesso.
        """
        # Tenta acessar endpoint que requer autenticação
        response = client.get("/api/atendimentos", headers=auth_headers_admin)
        
        # Deve permitir acesso (200) ou retornar lista vazia
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    

    def test_acesso_endpoint_protegido_sem_token(self, client: TestClient):
        """
        Testa acesso a endpoint protegido sem token.
        
        Deve retornar erro 401.
        """
        response = client.get("/api/atendimentos")
        
        assert response.status_code == 401
    

    def test_acesso_endpoint_protegido_token_invalido(self, client: TestClient):
        """
        Testa acesso a endpoint protegido com token inválido.
        
        Deve retornar erro 401.
        """
        headers = {"Authorization": "Bearer token_invalido"}
        response = client.get("/api/atendimentos", headers=headers)
        
        assert response.status_code == 401
    

    def test_acesso_admin_com_usuario_cliente(
        self, 
        client: TestClient, 
        auth_headers_cliente):
        """
        Testa acesso a endpoint de admin com usuário cliente.
        
        Deve retornar erro 403 (sem permissão).
        """
        # Endpoint que requer permissão de admin
        response = client.get("/api/atendimentos", headers=auth_headers_cliente)
        
        # Cliente não tem permissão para ver todos os atendimentos
        assert response.status_code == 403
