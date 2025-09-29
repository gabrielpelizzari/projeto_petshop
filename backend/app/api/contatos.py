from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import contato as contato_schema
from app.services import contato_service, cliente_service
from app.api import deps
from app.models import models

router = APIRouter()

@router.post("/clientes/{cliente_id}/contatos", response_model=contato_schema.Contato, tags=["Contatos"])
def create_contato(
    cliente_id: int,
    contato_in: contato_schema.ContatoCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Cria um novo contato para um cliente."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para adicionar contato a este cliente")

    return contato_service.create_contato_for_cliente(db=db, contato=contato_in, cliente_id=cliente_id)


@router.put("/contatos/{contato_id}", response_model=contato_schema.Contato, tags=["Contatos"])
def update_contato(
    contato_id: int,
    contato_in: contato_schema.ContatoUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Atualiza um contato."""
    db_contato = contato_service.get_contato(db, contato_id=contato_id)
    if not db_contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_contato.cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para atualizar este contato")

    return contato_service.update_contato(db=db, contato=db_contato, updates=contato_in)


@router.delete("/contatos/{contato_id}", status_code=status.HTTP_200_OK, tags=["Contatos"])
def delete_contato(
    contato_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):
    
    """Deleta um contato."""
    db_contato = contato_service.get_contato(db, contato_id=contato_id)
    if not db_contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_contato.cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para deletar este contato")

    contato_service.delete_contato(db=db, contato=db_contato)
    return {"detail": "Contato deletado com sucesso"}
