from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import endereco as endereco_schema
from app.services import endereco_service, cliente_service
from app.api import deps
from app.models import models

router = APIRouter()

@router.post("/clientes/{cliente_id}/enderecos", response_model=endereco_schema.Endereco, tags=["Endereços"])
def create_endereco(
    cliente_id: int,
    endereco_in: endereco_schema.EnderecoCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Cria um novo endereço para um cliente."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para adicionar endereço a este cliente")

    return endereco_service.create_endereco_for_cliente(db=db, endereco=endereco_in, cliente_id=cliente_id)


@router.put("/enderecos/{endereco_id}", response_model=endereco_schema.Endereco, tags=["Endereços"])
def update_endereco(
    endereco_id: int,
    endereco_in: endereco_schema.EnderecoUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):
    """Atualiza um endereço."""
    db_endereco = endereco_service.get_endereco(db, endereco_id=endereco_id)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_endereco.cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para atualizar este endereço")

    return endereco_service.update_endereco(db=db, endereco=db_endereco, updates=endereco_in)


@router.delete("/enderecos/{endereco_id}", status_code=status.HTTP_200_OK, tags=["Endereços"])
def delete_endereco(
    endereco_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):
    """Deleta um endereço."""
    db_endereco = endereco_service.get_endereco(db, endereco_id=endereco_id)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_endereco.cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para deletar este endereço")

    endereco_service.delete_endereco(db=db, endereco=db_endereco)
    return {"detail": "Endereço deletado com sucesso"}
