from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
from app.models import models
from app.api import usuarios, clientes, racas, auth, pets, contatos, enderecos, atendimentos, cadastro

# Cria as tabelas no banco de dados se não existirem
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API PetShop",
    description="API para gerenciamento de um petshop.",
    version="0.1.0"
)

# Configuração do CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Content-Type", "Authorization"], 
)

@app.get("/", tags=["Root"], summary="Verifica se a API está online")
def read_root():
    """Endpoint para verificar o status da API."""
    return {"status": "API is running"}


app.include_router(auth.router, prefix="/api")
app.include_router(usuarios.router, prefix="/api/usuarios")
app.include_router(clientes.router, prefix="/api/clientes")
app.include_router(racas.router, prefix="/api/racas", tags=["Raças"])
app.include_router(pets.admin_router, prefix="/api/pets")
app.include_router(pets.cliente_router, prefix="/api/clientes/{cliente_id}/pets")
app.include_router(contatos.router, prefix="/api")
app.include_router(enderecos.router, prefix="/api")
app.include_router(atendimentos.router, prefix="/api")
app.include_router(cadastro.router, prefix="/api/cadastro")
