from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import cliente as cliente_schema, pet as pet_schema, usuario as usuario_schema, contato as contato_schema
from app.services import cliente_service, usuario_service, endereco_service, contato_service
from app.api import deps
from app.models import models

router = APIRouter()

@router.post("/admin", response_model=cliente_schema.Cliente, status_code=status.HTTP_201_CREATED, tags=["Clientes"])
def admin_create_cliente(
    cliente_data: cliente_schema.AdminClienteCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)
):
    """Cria um novo cliente completo (usuário, cliente, endereço). Acesso de administrador."""
    db_usuario = usuario_service.get_usuario_by_cpf(db, cpf=cliente_data.cpf)
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF já cadastrado.")

    if contato_service.get_contato_by_valor(db, valor=cliente_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado.")

    if contato_service.get_contato_by_valor(db, valor=cliente_data.telefone):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Telefone já cadastrado.")

    try:
        nome_completo = f"{cliente_data.nome.strip()} {cliente_data.sobrenome.strip()}"
        usuario_to_create = usuario_schema.UsuarioCreate(
            cpf=cliente_data.cpf,
            nome=nome_completo,
            senha=cliente_data.senha,
            perfil=models.PerfilUsuario.CLIENTE)
        novo_usuario = usuario_service.create_usuario(db=db, usuario=usuario_to_create)

        if novo_usuario.cliente:
            endereco_service.create_endereco_for_cliente(
                db=db, 
                endereco=cliente_data.endereco, 
                cliente_id=novo_usuario.cliente.id)

            contato_service.create_contato_for_cliente(
                db=db,
                contato=contato_schema.ContatoCreate(tipo='email', valor=cliente_data.email, tag='Principal'),
                cliente_id=novo_usuario.cliente.id)

            contato_service.create_contato_for_cliente(
                db=db,
                contato=contato_schema.ContatoCreate(tipo='telefone', valor=cliente_data.telefone, tag='Principal'),
                cliente_id=novo_usuario.cliente.id)
        
        db.commit()
        db.refresh(novo_usuario.cliente)
        return novo_usuario.cliente

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno ao processar o cadastro: {e}"
        )


@router.get("/", response_model=list[cliente_schema.ClienteAdminResponse], tags=["Clientes"])
def read_clientes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.Usuario = Depends(deps.get_current_active_admin)
):
    """Lista todos os clientes. Acesso restrito a administradores."""
    clientes = cliente_service.get_clientes(db, skip=skip, limit=limit)
    return clientes


@router.get("/me", response_model=cliente_schema.Cliente, tags=["Clientes"])
def read_cliente_me(
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Obtém os dados do cliente logado."""
    if current_user.perfil != models.PerfilUsuario.CLIENTE:
        raise HTTPException(status_code=403, detail="Apenas clientes podem acessar esta rota")

    cliente = cliente_service.get_cliente_by_cpf(db, cpf=current_user.cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Dados do cliente não encontrados")
    return cliente

@router.get("/me/pets", response_model=list[pet_schema.Pet], tags=["Clientes"])
def read_cliente_me_pets(
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Obtém a lista de pets do cliente logado."""
    if current_user.perfil != models.PerfilUsuario.CLIENTE:
        raise HTTPException(status_code=403, detail="Apenas clientes podem acessar esta rota")

    cliente = cliente_service.get_cliente_by_cpf(db, cpf=current_user.cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Dados do cliente não encontrados")

    return cliente.pets


@router.get("/{cliente_id}", response_model=cliente_schema.Cliente, tags=["Clientes"])
def read_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Obtém os dados de um cliente específico."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")

    # Regra de permissão
    if current_user.perfil != models.PerfilUsuario.ADMIN and db_cliente.cpf != current_user.cpf:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para ver este cliente")
    
    return db_cliente


@router.put("/admin/{cliente_id}", response_model=cliente_schema.Cliente, tags=["Clientes"])
def admin_update_cliente(
    cliente_id: int,
    updates: cliente_schema.AdminClienteUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):

    """Atualiza os dados de um cliente (nome, senha, endereço). Acesso de administrador."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")

    try:
        # Atualiza nome e sobrenome se fornecidos
        if updates.nome or updates.sobrenome:
            nome_completo = f"{(updates.nome or db_cliente.nome.split(' ')[0]).strip()} {(updates.sobrenome or ' '.join(db_cliente.nome.split(' ')[1:])).strip()}".strip()
            usuario_service.admin_update_usuario(db=db, usuario=db_cliente.usuario, updates=usuario_schema.AdminUsuarioUpdate(nome=nome_completo))

        # Atualiza a senha se fornecida
        if updates.nova_senha:
            usuario_service.admin_update_usuario(db=db, usuario=db_cliente.usuario, updates=usuario_schema.AdminUsuarioUpdate(nova_senha=updates.nova_senha))

        # Atualiza o endereço se fornecido (assumindo que o cliente tem pelo menos um)
        if updates.endereco and db_cliente.enderecos:
            endereco_principal = db_cliente.enderecos[0]
            endereco_service.update_endereco(db, endereco=endereco_principal, updates=updates.endereco)

        # Atualiza o email principal se fornecido
        if updates.email:
            contato_service.update_or_create_principal_contato(db, cliente_id=db_cliente.id, tipo='email', valor=updates.email)

        # Atualiza o telefone principal se fornecido
        if updates.telefone:
            contato_service.update_or_create_principal_contato(db, cliente_id=db_cliente.id, tipo='telefone', valor=updates.telefone)
        
        db.commit()
        db.refresh(db_cliente)
        return db_cliente

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno ao atualizar o cliente: {e}")


@router.put("/me", response_model=cliente_schema.Cliente, tags=["Clientes"])
def update_my_profile(
    updates: cliente_schema.ClienteUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):
    """Permite ao cliente atualizar seus próprios dados (nome, senha, email, telefone, endereço)."""
    # Verifica se o usuário atual é um cliente
    if not current_user.cliente:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas clientes podem atualizar seu perfil.")
    
    db_cliente = current_user.cliente

    try:
        # Atualiza nome e sobrenome se fornecidos
        if updates.nome or updates.sobrenome:
            nome_completo = f"{(updates.nome or db_cliente.nome.split(' ')[0]).strip()} {(updates.sobrenome or ' '.join(db_cliente.nome.split(' ')[1:])).strip()}".strip()
            usuario_service.admin_update_usuario(db=db, usuario=db_cliente.usuario, updates=usuario_schema.AdminUsuarioUpdate(nome=nome_completo))

        # Atualiza a senha se fornecida
        if updates.nova_senha:
            usuario_service.admin_update_usuario(db=db, usuario=db_cliente.usuario, updates=usuario_schema.AdminUsuarioUpdate(nova_senha=updates.nova_senha))

        # Atualiza o endereço se fornecido (assumindo que o cliente tem pelo menos um)
        if updates.endereco and db_cliente.enderecos:
            endereco_principal = db_cliente.enderecos[0]
            endereco_service.update_endereco(db, endereco=endereco_principal, updates=updates.endereco)

        # Atualiza o email principal se fornecido
        if updates.email:
            contato_service.update_or_create_principal_contato(db, cliente_id=db_cliente.id, tipo='email', valor=updates.email)

        # Atualiza o telefone principal se fornecido
        if updates.telefone:
            contato_service.update_or_create_principal_contato(db, cliente_id=db_cliente.id, tipo='telefone', valor=updates.telefone)
        
        db.commit()
        db.refresh(db_cliente)
        return db_cliente

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno ao atualizar o perfil: {e}")


@router.put("/{cliente_id}", response_model=cliente_schema.Cliente, tags=["Clientes"])
def update_cliente(
    cliente_id: int,
    cliente_in: cliente_schema.ClienteUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Atualiza os dados de um cliente."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")

    # Regra de permissão
    if current_user.perfil != models.PerfilUsuario.ADMIN and db_cliente.cpf != current_user.cpf:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para atualizar este cliente")

    cliente = cliente_service.update_cliente(db=db, cliente=db_cliente, updates=cliente_in)
    return cliente


@router.delete("/{cliente_id}", status_code=status.HTTP_200_OK, tags=["Clientes"])
def delete_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):
    
    """Deleta um cliente e seu usuário associado. Acesso restrito a administradores."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")

    # Encontra o usuário associado para deletá-lo (a cascata removerá o cliente)
    db_usuario = usuario_service.get_usuario_by_cpf(db, cpf=db_cliente.cpf)
    if db_usuario is None:
        # Isso indica uma inconsistência de dados, mas tratamos para evitar crash
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário associado não encontrado")

    usuario_service.delete_usuario(db=db, usuario=db_usuario)
    return {"detail": "Cliente e usuário associado deletados com sucesso"}

