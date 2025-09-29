from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import raca as raca_schema
from app.services import raca_service
from app.api import deps
from app.models import models

router = APIRouter()

@router.post("/", response_model=raca_schema.Raca, tags=["Raças"])
def create_raca(
    raca_in: raca_schema.RacaCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):

    """Cria uma nova raça. Acesso restrito a administradores."""
    db_raca = raca_service.get_raca_by_nome(db, nome=raca_in.nome)
    if db_raca:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Raça com este nome já existe.")
    return raca_service.create_raca(db=db, raca=raca_in)


@router.get("/", response_model=list[raca_schema.Raca], tags=["Raças"])
def read_racas(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Lista todas as raças. Acesso para qualquer usuário autenticado."""
    racas = raca_service.get_racas(db, skip=skip, limit=limit)
    return racas


@router.put("/{raca_id}", response_model=raca_schema.Raca, tags=["Raças"])
def update_raca(
    raca_id: int,
    raca_in: raca_schema.RacaUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):

    """Atualiza uma raça. Acesso restrito a administradores."""
    db_raca = raca_service.get_raca(db, raca_id=raca_id)
    if db_raca is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Raça não encontrada")
    
    # Verifica se já existe outra raça com o mesmo nome
    existing_raca = raca_service.get_raca_by_nome(db, nome=raca_in.nome)
    if existing_raca and existing_raca.id != raca_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe uma raça com este nome.")
    
    return raca_service.update_raca(db=db, db_raca=db_raca, raca_update=raca_in)


@router.delete("/{raca_id}", status_code=status.HTTP_200_OK, tags=["Raças"])
def delete_raca(
    raca_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):

    """Deleta uma raça. Acesso restrito a administradores."""
    db_raca = raca_service.get_raca(db, raca_id=raca_id)
    if db_raca is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Raça não encontrada")
    
    raca_service.delete_raca(db=db, raca=db_raca)
    return {"detail": "Raça deletada com sucesso"}
