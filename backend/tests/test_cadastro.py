"""
Testes para a API de cadastro.

Testa a criação de novos usuários com dados completos.
"""

from fastapi.testclient import TestClient


class TestCadastro:
    """Testes para cadastro de usuários."""
    
    def test_cadastro_sucesso(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com dados válidos.
        
        Deve criar usuário, cliente, endereço e contatos.
        """
        response = client.post("/api/cadastro/", json=dados_cadastro_valido)
        
        # Verifica se o cadastro foi bem-sucedido
        assert response.status_code == 201
        
        # Verifica os dados retornados
        data = response.json()
        assert data["cpf"] == dados_cadastro_valido["cpf"]
        assert data["nome"] == f"{dados_cadastro_valido['nome']} {dados_cadastro_valido['sobrenome']}"
        assert "senha" not in data  # Senha não deve ser retornada
        assert data["perfil"] == "cliente"  # Enum retorna valor em minúsculo
        
        # O schema Usuario não retorna o relacionamento cliente
        # Mas verifica se o usuário foi criado corretamente
        assert "cpf" in data
        assert "nome" in data
        assert "perfil" in data
    

    def test_cadastro_cpf_duplicado(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com CPF já existente.
        
        Deve retornar erro 400.
        """
        # Primeiro cadastro
        client.post("/api/cadastro/", json=dados_cadastro_valido)
        
        # Segundo cadastro com mesmo CPF
        response = client.post("/api/cadastro/", json=dados_cadastro_valido)
        
        assert response.status_code == 400
        assert "CPF já cadastrado" in response.json()["detail"]
    

    def test_cadastro_email_duplicado(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com email já existente.
        
        Deve retornar erro 400.
        """
        # Primeiro cadastro
        client.post("/api/cadastro/", json=dados_cadastro_valido)
        
        # Segundo cadastro com mesmo email, mas CPF diferente
        dados_segundo = dados_cadastro_valido.copy()
        dados_segundo["cpf"] = "98765432100"
        
        response = client.post("/api/cadastro/", json=dados_segundo)
        
        assert response.status_code == 400
        assert "E-mail já cadastrado" in response.json()["detail"]
    

    def test_cadastro_telefone_duplicado(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com telefone já existente.
        
        Deve retornar erro 400.
        """
        # Primeiro cadastro
        client.post("/api/cadastro/", json=dados_cadastro_valido)
        
        # Segundo cadastro com mesmo telefone, mas CPF e email diferentes
        dados_segundo = dados_cadastro_valido.copy()
        dados_segundo["cpf"] = "98765432100"
        dados_segundo["email"] = "outro@teste.com"
        
        response = client.post("/api/cadastro/", json=dados_segundo)
        
        assert response.status_code == 400
        assert "Telefone já cadastrado" in response.json()["detail"]
    
    
    def test_cadastro_dados_obrigatorios_faltando(self, client: TestClient):
        """
        Testa cadastro com dados obrigatórios faltando.
        
        Deve retornar erro 422 (validação).
        """
        dados_incompletos = {
            "nome": "João",
            # faltando sobrenome, cpf, senha, etc.
        }
        
        response = client.post("/api/cadastro/", json=dados_incompletos)
        
        assert response.status_code == 422
    

    def test_cadastro_cpf_formato_invalido(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com CPF em formato inválido.
        
        Deve retornar erro 422 com a nova validação.
        """
        dados_invalidos = dados_cadastro_valido.copy()
        dados_invalidos["cpf"] = "123"  # CPF muito curto
        
        response = client.post("/api/cadastro/", json=dados_invalidos)
        
        assert response.status_code == 422
        assert "CPF deve ter exatamente 11 dígitos" in str(response.json())
    

    def test_cadastro_email_formato_invalido(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com email em formato inválido.
        
        Deve retornar erro 422 com a nova validação.
        """
        dados_invalidos = dados_cadastro_valido.copy()
        dados_invalidos["email"] = "email_invalido"  # Sem @
        
        response = client.post("/api/cadastro/", json=dados_invalidos)
        
        assert response.status_code == 422
    

    def test_cadastro_senha_muito_curta(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro com senha muito curta.
        
        Deve retornar erro de validação se houver validação de senha.
        """
        dados_invalidos = dados_cadastro_valido.copy()
        dados_invalidos["senha"] = "123"  # Senha muito curta
        
        response = client.post("/api/cadastro/", json=dados_invalidos)
        
        assert response.status_code == 422
        assert "Senha deve ter pelo menos 6 caracteres" in str(response.json())
    
    
    def test_cadastro_endereco_obrigatorio(self, client: TestClient, dados_cadastro_valido):
        """
        Testa cadastro sem endereço.
        
        Deve retornar erro de validação.
        """
        dados_sem_endereco = dados_cadastro_valido.copy()
        del dados_sem_endereco["endereco"]
        
        response = client.post("/api/cadastro/", json=dados_sem_endereco)
        
        assert response.status_code == 422
