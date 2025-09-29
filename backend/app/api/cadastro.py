from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import cadastro as cadastro_schema, usuario as usuario_schema
from app.services import usuario_service, endereco_service, contato_service
from app.schemas import contato as contato_schema
from app.models import models

router = APIRouter()

@router.post("/", response_model=usuario_schema.Usuario, status_code=status.HTTP_201_CREATED, tags=["Cadastro"])
def create_cadastro_completo(
    cadastro_data: cadastro_schema.CadastroCompleto,
    db: Session = Depends(get_db)):
    """Cria um novo usuário, cliente e endereço em uma única transação."""
    db_usuario = usuario_service.get_usuario_by_cpf(db, cpf=cadastro_data.cpf)
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF já cadastrado.")

    # Verifica se o email já está em uso
    if contato_service.get_contato_by_valor(db, valor=cadastro_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado.")

    # Verifica se o telefone já está em uso
    if contato_service.get_contato_by_valor(db, valor=cadastro_data.telefone):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Telefone já cadastrado.")

    try:
        # Cria o usuário (que também cria o cliente via trigger/automação no service)
        nome_completo = f"{cadastro_data.nome.strip()} {cadastro_data.sobrenome.strip()}"
        usuario_to_create = usuario_schema.UsuarioCreate(
            cpf=cadastro_data.cpf,
            nome=nome_completo,
            senha=cadastro_data.senha,
            perfil=models.PerfilUsuario.CLIENTE)
        novo_usuario = usuario_service.create_usuario(db=db, usuario=usuario_to_create)

        # Adiciona o endereço para o cliente recém-criado
        # O cliente é acessível através do relacionamento no objeto do usuário
        if novo_usuario.cliente:
            # Adiciona o endereço
            endereco_service.create_endereco_for_cliente(
                db=db, 
                endereco=cadastro_data.endereco, 
                cliente_id=novo_usuario.cliente.id)

            # Adiciona o email
            contato_service.create_contato_for_cliente(
                db=db,
                contato=contato_schema.ContatoCreate(tipo='email', valor=cadastro_data.email, tag='Principal'),
                cliente_id=novo_usuario.cliente.id)

            # Adiciona o telefone
            contato_service.create_contato_for_cliente(
                db=db,
                contato=contato_schema.ContatoCreate(tipo='telefone', valor=cadastro_data.telefone, tag='Principal'),
                cliente_id=novo_usuario.cliente.id)
        
        db.commit()
        db.refresh(novo_usuario)
        return novo_usuario

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno ao processar o cadastro: {e}")
