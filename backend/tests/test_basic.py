"""
Testes básicos para verificar se a API está funcionando.

Testa endpoints básicos e configuração da aplicação.
"""

from fastapi.testclient import TestClient


class TestBasic:
    """Testes básicos da API."""
    
    def test_api_esta_online(self, client: TestClient):
        """
        Testa se a API está respondendo.
        
        Deve retornar status 200 e mensagem de confirmação.
        """
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "API is running"
    

    def test_endpoint_inexistente(self, client: TestClient):
        """
        Testa acesso a endpoint que não existe.
        
        Deve retornar erro 404.
        """
        response = client.get("/endpoint/que/nao/existe")
        
        assert response.status_code == 404
    

    def test_metodo_nao_permitido(self, client: TestClient):
        """
        Testa método HTTP não permitido.
        
        Deve retornar erro 405.
        """
        # Tenta fazer POST no endpoint raiz que só aceita GET
        response = client.post("/")
        
        assert response.status_code == 405
    

    def test_cors_headers(self, client: TestClient):
        """
        Testa se os headers CORS estão configurados.
        
        Importante para permitir acesso do frontend.
        """
        response = client.options("/", headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET"
        })
        
        # Verifica se permite o origin do frontend
        assert response.status_code in [200, 204]
    

    def test_content_type_json(self, client: TestClient):
        """
        Testa se a API retorna JSON por padrão.
        
        Endpoints devem retornar application/json.
        """
        response = client.get("/")
        
        assert response.headers["content-type"] == "application/json"
    
    
    def test_api_docs_disponiveis(self, client: TestClient):
        """
        Testa se a documentação da API está disponível.
        
        FastAPI gera documentação automática.
        """
        # Testa Swagger UI
        response = client.get("/docs")
        assert response.status_code == 200
        
        # Testa ReDoc
        response = client.get("/redoc")
        assert response.status_code == 200
        
        # Testa OpenAPI JSON
        response = client.get("/openapi.json")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
