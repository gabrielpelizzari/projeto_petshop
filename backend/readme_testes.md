# 🧪 Guia Rápido - Testes Unitários

## Comandos Essenciais

```bash
# 1. Instalar dependências de teste
uv sync --group dev

# 2. Executar todos os testes
uv run pytest

# 3. Executar com detalhes
uv run pytest -v

# 4. Executar teste específico
uv run pytest tests/test_auth.py

# 5. Executar com cobertura
uv run pytest --cov=app
```

## Estrutura dos Testes

```
tests/
├── conftest.py           # ⚙️ Configurações globais
├── test_basic.py         # 🔧 Testes básicos da API
├── test_auth.py          # 🔐 Testes de login/autenticação
├── test_cadastro.py      # 👤 Testes de cadastro
├── test_pets.py          # 🐕 Testes de pets
└── test_atendimentos.py  # 📋 Testes de atendimentos
```

## O que cada teste faz

### **test_basic.py** - Testes Fundamentais

- ✅ API está online (`/`)
- ✅ Endpoints inexistentes retornam 404
- ✅ CORS configurado
- ✅ Documentação disponível (`/docs`)

### **test_auth.py** - Autenticação

- ✅ Login com CPF e senha válidos
- ✅ Login com credenciais inválidas
- ✅ Acesso a endpoints protegidos
- ✅ Validação de permissões (admin vs cliente)

### **test_cadastro.py** - Cadastro de Usuários

- ✅ Cadastro completo com dados válidos
- ✅ Validação de CPF duplicado
- ✅ Validação de email duplicado
- ✅ Validação de campos obrigatórios

### **test_pets.py** - Gerenciamento de Pets

- ✅ Criar pet para cliente
- ✅ Listar pets (admin vê todos, cliente vê seus)
- ✅ Validação de raças existentes
- ✅ Controle de permissões

### **test_atendimentos.py** - Atendimentos

- ✅ Criar atendimento para pet
- ✅ Listar atendimentos (admin vê todos)
- ✅ Atualizar e excluir atendimentos
- ✅ Validação de dados obrigatórios

## 🔧 Como Funciona

### **Banco de Dados de Teste**

- Cada teste usa um banco **SQLite em memória**
- Dados são **criados e destruídos** automaticamente
- **Isolamento completo** entre testes

### **Autenticação Automática**

- Fixtures criam usuários de teste automaticamente
- Tokens JWT são gerados automaticamente
- Headers de autorização prontos para usar

### **Dados de Teste**

- Fixtures fornecem dados válidos
- Reutilizáveis em múltiplos testes
- Consistentes e confiáveis

## 📊 Exemplos Práticos

### **Teste Simples**

```python
def test_api_online(client):
    response = client.get("/")
    assert response.status_code == 200
```

### **Teste com Autenticação**

```python
def test_criar_pet(client, auth_headers_cliente, usuario_cliente, dados_pet_valido):
    response = client.post(
        f"/api/clientes/{usuario_cliente.cliente.id}/pets/",
        json=dados_pet_valido,
        headers=auth_headers_cliente
    )
    assert response.status_code == 200
```

## Cenários Testados

### **✅ Casos de Sucesso**

- Operações com dados válidos
- Autenticação correta
- Permissões adequadas

### **❌ Casos de Erro**

- Dados inválidos ou faltando
- Credenciais incorretas
- Acesso sem permissão
- Recursos inexistentes

### **🔒 Segurança**

- Controle de acesso por perfil
- Validação de tokens
- Proteção de dados sensíveis

## Comandos de Debug

```bash
# Para no primeiro erro
uv run pytest -x

# Mostra prints e detalhes
uv run pytest -s -v

# Teste específico com debug
uv run pytest tests/test_auth.py::TestAuth::test_login_sucesso -vv -s
```

## Relatório de Cobertura

```bash
# Gera relatório HTML
uv run pytest --cov=app --cov-report=html

# Abre no navegador (Windows)
start htmlcov/index.html
```

## Como verificar se esta tudo funcionando corretamente

```bash
# 1. Teste básico
uv run pytest tests/test_basic.py::TestBasic::test_api_esta_online -v

# 2. Teste geral
uv run pytest -v

# 3. Resultado esperado:
# ✅ tests/test_basic.py::TestBasic::test_api_esta_online PASSED
# ✅ tests/test_auth.py::TestAuth::test_login_sucesso PASSED
# ✅ tests/test_cadastro.py::TestCadastro::test_cadastro_sucesso PASSED
```
