"""
Testes para a API de atendimentos.

Testa criação, listagem, atualização e exclusão de atendimentos.
"""

from fastapi.testclient import TestClient


class TestAtendimentos:
    """Testes para gerenciamento de atendimentos."""
    
    def test_listar_todos_atendimentos_admin(
        self, 
        client: TestClient, 
        auth_headers_admin):
        """
        Testa listagem de todos os atendimentos (acesso admin).
        
        Admin deve conseguir ver todos os atendimentos do sistema.
        """
        response = client.get("/api/atendimentos", headers=auth_headers_admin)
        
        assert response.status_code == 200
        atendimentos = response.json()
        assert isinstance(atendimentos, list)
    

    def test_listar_atendimentos_sem_permissao(
        self, 
        client: TestClient, 
        auth_headers_cliente):
        """
        Testa listagem de todos os atendimentos sem permissão de admin.
        
        Cliente não deve conseguir ver todos os atendimentos.
        """
        response = client.get("/api/atendimentos", headers=auth_headers_cliente)
        
        assert response.status_code == 403
    

    def test_criar_atendimento_sucesso(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        dados_pet_valido,
        dados_atendimento_valido):
        """
        Testa criação de atendimento com dados válidos.
        
        Admin deve conseguir criar atendimento para qualquer pet.
        """
        # Primeiro, cria um pet
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin)
        pet = pet_response.json()
        pet_id = pet["id"]
        
        # Cria o atendimento
        response = client.post(
            f"/api/pets/{pet_id}/atendimentos",
            json=dados_atendimento_valido,
            headers=auth_headers_admin)
        
        assert response.status_code == 200
        atendimento = response.json()
        assert atendimento["descricao"] == dados_atendimento_valido["descricao"]
        assert atendimento["valor"] == dados_atendimento_valido["valor"]
        assert atendimento["data"] == dados_atendimento_valido["data"]
        assert atendimento["pet_id"] == pet_id
    

    def test_criar_atendimento_pet_inexistente(
        self, 
        client: TestClient, 
        auth_headers_admin,
        dados_atendimento_valido):
        """
        Testa criação de atendimento para pet inexistente.
        
        Deve retornar erro 404.
        """
        pet_id_inexistente = 99999
        
        response = client.post(
            f"/api/pets/{pet_id_inexistente}/atendimentos",
            json=dados_atendimento_valido,
            headers=auth_headers_admin)
        
        assert response.status_code == 404
        assert "Pet não encontrado" in response.json()["detail"]
    

    def test_criar_atendimento_dados_obrigatorios_faltando(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        dados_pet_valido):
        """
        Testa criação de atendimento com dados obrigatórios faltando.
        
        Deve retornar erro 422.
        """
        # Cria um pet primeiro
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin)
        pet_id = pet_response.json()["id"]
        
        # Dados incompletos
        atendimento_incompleto = {
            "descricao": "Consulta"
            # faltando valor e data
        }
        
        response = client.post(
            f"/api/pets/{pet_id}/atendimentos",
            json=atendimento_incompleto,
            headers=auth_headers_admin)
        
        assert response.status_code == 422
    

    def test_criar_atendimento_valor_negativo(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        dados_pet_valido):
        """
        Testa criação de atendimento com valor negativo.
        
        Deve retornar erro de validação se houver validação de valor.
        """
        # Cria um pet primeiro
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin)
        pet_id = pet_response.json()["id"]
        
        atendimento_data = {
            "descricao": "Consulta",
            "valor": -50.00,  # Valor negativo
            "data": "2024-01-15"
        }
        
        response = client.post(
            f"/api/pets/{pet_id}/atendimentos",
            json=atendimento_data,
            headers=auth_headers_admin)
        
        # Agora a API valida valor negativo
        assert response.status_code == 422
        assert "Valor do atendimento deve ser positivo" in str(response.json())
    

    def test_criar_atendimento_descricao_vazia(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        dados_pet_valido):
        """
        Testa criação de atendimento com descrição vazia.
        
        Deve retornar erro 422 com a nova validação.
        """
        # Cria um pet primeiro
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin)
        pet_id = pet_response.json()["id"]
        
        atendimento_data = {
            "descricao": "",  # Descrição vazia
            "valor": 100.00,
            "data": "2024-01-15"
        }
        
        response = client.post(
            f"/api/pets/{pet_id}/atendimentos",
            json=atendimento_data,
            headers=auth_headers_admin)
        
        # Agora a API valida descrição vazia
        assert response.status_code == 422
        assert "Descrição do atendimento não pode estar vazia" in str(response.json())
    

    def test_listar_atendimentos_do_pet(
        self, 
        client: TestClient, 
        auth_headers_cliente,
        usuario_cliente,
        dados_pet_valido,
        dados_atendimento_valido):
        """
        Testa listagem de atendimentos de um pet específico.
        
        Cliente deve conseguir ver atendimentos dos seus pets.
        """
        # Cria um pet
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_cliente)
        pet_id = pet_response.json()["id"]
        
        # Cria um atendimento (como admin para ter permissão)
        
        # Lista os atendimentos do pet
        response = client.get(
            f"/api/pets/{pet_id}/atendimentos",
            headers=auth_headers_cliente)
        
        assert response.status_code == 200
        atendimentos = response.json()
        assert isinstance(atendimentos, list)
    

    def test_atualizar_atendimento_sucesso(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        dados_pet_valido,
        dados_atendimento_valido):
        """
        Testa atualização de atendimento com dados válidos.
        
        Admin deve conseguir atualizar qualquer atendimento.
        """
        # Cria um pet
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin)
        pet_id = pet_response.json()["id"]
        
        # Cria um atendimento
        atendimento_response = client.post(
            f"/api/pets/{pet_id}/atendimentos",
            json=dados_atendimento_valido,
            headers=auth_headers_admin)
        atendimento_id = atendimento_response.json()["id"]
        
        # Atualiza o atendimento
        dados_atualizados = {
            "descricao": "Consulta atualizada",
            "valor": 200.00,
            "data": "2024-01-20"
        }
        
        response = client.put(
            f"/api/atendimentos/{atendimento_id}",
            json=dados_atualizados,
            headers=auth_headers_admin)
        
        assert response.status_code == 200
        atendimento_atualizado = response.json()
        assert atendimento_atualizado["descricao"] == dados_atualizados["descricao"]
        assert atendimento_atualizado["valor"] == dados_atualizados["valor"]
    

    def test_excluir_atendimento_sucesso(
        self, 
        client: TestClient, 
        auth_headers_admin,
        usuario_cliente,
        dados_pet_valido,
        dados_atendimento_valido):
        """
        Testa exclusão de atendimento.
        
        Admin deve conseguir excluir qualquer atendimento.
        """
        # Cria um pet
        pet_response = client.post(
            f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
            json=dados_pet_valido,
            headers=auth_headers_admin)
        pet_id = pet_response.json()["id"]
        
        # Cria um atendimento
        atendimento_response = client.post(
            f"/api/pets/{pet_id}/atendimentos",
            json=dados_atendimento_valido,
            headers=auth_headers_admin)
        atendimento_id = atendimento_response.json()["id"]
        
        # Exclui o atendimento
        response = client.delete(
            f"/api/atendimentos/{atendimento_id}",
            headers=auth_headers_admin)
        
        assert response.status_code == 200
        data = response.json()
        assert "deletado com sucesso" in data["detail"]
        
        # Verifica se foi excluído tentando excluir novamente
        second_delete = client.delete(
            f"/api/atendimentos/{atendimento_id}",
            headers=auth_headers_admin)
        assert second_delete.status_code == 404
