# Testes Unitários - API PetShop

Este diretório contém todos os testes unitários para a API do PetShop. Os testes são escritos usando **pytest** e **FastAPI TestClient**.

## 📋 Estrutura dos Testes

```
tests/
├── conftest.py              # Configurações e fixtures globais
├── test_basic.py            # Testes básicos da API
├── test_auth.py             # Testes de autenticação
├── test_cadastro.py         # Testes de cadastro de usuários
├── test_pets.py             # Testes de gerenciamento de pets
├── test_atendimentos.py     # Testes de atendimentos
└── README.md                # Este arquivo
```

## 🚀 Como Executar os Testes

### 1. Instalar Dependências

```bash
# Instala as dependências de desenvolvimento
uv sync --group dev
```

### 2. Executar Todos os Testes

```bash
# Executa todos os testes
uv run pytest

# Executa com mais detalhes
uv run pytest -v

# Executa com relatório de cobertura
uv run pytest --cov=app
```

### 3. Executar Testes Específicos

```bash
# Executa apenas testes de autenticação
uv run pytest tests/test_auth.py

# Executa apenas testes de pets
uv run pytest tests/test_pets.py

# Executa um teste específico
uv run pytest tests/test_auth.py::TestAuth::test_login_sucesso
```

### 4. Executar Testes em Modo Watch

```bash
# Executa testes automaticamente quando arquivos mudam
uv run pytest-watch
```

## 🧪 Tipos de Testes

### **Testes Básicos** (`test_basic.py`)
- ✅ API está online
- ✅ Endpoints inexistentes retornam 404
- ✅ CORS configurado corretamente
- ✅ Documentação disponível

### **Testes de Autenticação** (`test_auth.py`)
- ✅ Login com credenciais válidas
- ✅ Login com credenciais inválidas
- ✅ Acesso a endpoints protegidos
- ✅ Validação de tokens
- ✅ Controle de permissões (admin vs cliente)

### **Testes de Cadastro** (`test_cadastro.py`)
- ✅ Cadastro com dados válidos
- ✅ Validação de CPF duplicado
- ✅ Validação de email duplicado
- ✅ Validação de telefone duplicado
- ✅ Validação de campos obrigatórios
- ✅ Validação de formatos (CPF, email)

### **Testes de Pets** (`test_pets.py`)
- ✅ Criação de pets
- ✅ Listagem de pets
- ✅ Validação de permissões
- ✅ Validação de dados obrigatórios
- ✅ Validação de raças existentes

### **Testes de Atendimentos** (`test_atendimentos.py`)
- ✅ Criação de atendimentos
- ✅ Listagem de atendimentos
- ✅ Atualização de atendimentos
- ✅ Exclusão de atendimentos
- ✅ Validação de permissões

## 🔧 Configuração dos Testes

### **Banco de Dados de Teste**
- Usa **SQLite em memória** para isolamento
- Cada teste roda com banco limpo
- Dados são criados e destruídos automaticamente

### **Autenticação nos Testes**
- Fixtures criam usuários de teste (admin e cliente)
- Tokens JWT são gerados automaticamente
- Headers de autorização são fornecidos via fixtures

### **Dados de Teste**
- Fixtures fornecem dados válidos para testes
- Dados são consistentes e reutilizáveis
- Factory Boy pode ser usado para dados mais complexos

## 📊 Fixtures Disponíveis

### **Banco de Dados**
- `db`: Sessão de banco de dados de teste
- `client`: Cliente HTTP para fazer requisições

### **Usuários**
- `usuario_admin`: Usuário administrador
- `usuario_cliente`: Usuário cliente
- `token_admin`: Token JWT para admin
- `token_cliente`: Token JWT para cliente
- `auth_headers_admin`: Headers de autorização para admin
- `auth_headers_cliente`: Headers de autorização para cliente

### **Dados de Teste**
- `raca_teste`: Raça de cachorro para testes
- `dados_cadastro_valido`: Dados válidos para cadastro
- `dados_pet_valido`: Dados válidos para pet
- `dados_atendimento_valido`: Dados válidos para atendimento

## 🎯 Exemplos de Uso

### **Teste Simples**
```python
def test_api_online(client):
    response = client.get("/")
    assert response.status_code == 200
```

### **Teste com Autenticação**
```python
def test_listar_pets(client, auth_headers_admin):
    response = client.get("/api/pets/", headers=auth_headers_admin)
    assert response.status_code == 200
```

### **Teste com Dados**
```python
def test_criar_pet(client, auth_headers_cliente, usuario_cliente, dados_pet_valido):
    response = client.post(
        f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
        json=dados_pet_valido,
        headers=auth_headers_cliente
    )
    assert response.status_code == 200
```

## 📈 Relatórios de Cobertura

```bash
# Gera relatório de cobertura
uv run pytest --cov=app --cov-report=html

# Abre o relatório no navegador
open htmlcov/index.html
```

## 🐛 Debugging

### **Executar com Debugging**
```bash
# Para no primeiro erro
uv run pytest -x

# Mostra print statements
uv run pytest -s

# Modo verbose com detalhes
uv run pytest -vv
```

### **Executar Teste Específico com Debug**
```bash
uv run pytest tests/test_auth.py::TestAuth::test_login_sucesso -vv -s
```

## 📝 Boas Práticas

### **Nomenclatura**
- Arquivos: `test_*.py`
- Classes: `TestNomeDoModulo`
- Métodos: `test_acao_esperada`

### **Estrutura do Teste**
```python
def test_acao_esperada(self, client, fixtures_necessarias):
    """
    Descrição do que o teste faz.
    
    Deve explicar o comportamento esperado.
    """
    # Arrange (preparar dados)
    dados = {"campo": "valor"}
    
    # Act (executar ação)
    response = client.post("/endpoint", json=dados)
    
    # Assert (verificar resultado)
    assert response.status_code == 200
    assert response.json()["campo"] == "valor"
```

### **Isolamento**
- Cada teste deve ser independente
- Não depender da ordem de execução
- Limpar dados após cada teste

### **Cobertura**
- Testar casos de sucesso
- Testar casos de erro
- Testar validações
- Testar permissões

## 🔍 Troubleshooting

### **Erro: "Table already exists"**
- Problema: Banco não está sendo limpo entre testes
- Solução: Verificar fixture `db` no `conftest.py`

### **Erro: "Permission denied"**
- Problema: Token inválido ou permissões incorretas
- Solução: Verificar fixtures de autenticação

### **Erro: "Foreign key constraint"**
- Problema: Ordem de criação de dados relacionados
- Solução: Criar dependências antes (ex: raça antes de pet)

### **Testes Lentos**
- Usar banco em memória (SQLite)
- Evitar operações desnecessárias
- Usar fixtures com escopo apropriado

## 📚 Recursos Adicionais

- [Documentação do Pytest](https://docs.pytest.org/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Factory Boy](https://factoryboy.readthedocs.io/)
- [Coverage.py](https://coverage.readthedocs.io/)
