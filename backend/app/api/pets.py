from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import pet as pet_schema
from app.services import pet_service, cliente_service, raca_service, atendimento_service
from app.models import models
from app.api import deps

admin_router = APIRouter()
cliente_router = APIRouter()


@admin_router.get("/", response_model=list[pet_schema.Pet], tags=["Pets Admin"])
def read_all_pets(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):
    """Lista todos os pets do sistema. Acesso de administrador."""
    return pet_service.get_all_pets(db, skip=skip, limit=limit)


@cliente_router.post("/", response_model=pet_schema.Pet, tags=["Pets Cliente"])
def create_pet(
    cliente_id: int,
    pet_in: pet_schema.PetCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Cria um novo pet para um cliente."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para adicionar pet a este cliente")

    if not raca_service.get_raca(db, raca_id=pet_in.raca_id):
        raise HTTPException(status_code=404, detail="Raça não encontrada")

    return pet_service.create_pet_for_cliente(db=db, pet=pet_in, cliente_id=cliente_id)


@cliente_router.get("/", response_model=list[pet_schema.Pet], tags=["Pets Cliente"])
def read_pets_from_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Lista os pets de um cliente."""
    db_cliente = cliente_service.get_cliente(db, cliente_id=cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para ver os pets deste cliente")

    return pet_service.get_pets_by_cliente(db=db, cliente_id=cliente_id)


@admin_router.put("/{pet_id}", response_model=pet_schema.Pet, tags=["Pets Admin"])
def update_pet(
    pet_id: int,
    pet_in: pet_schema.PetUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Atualiza um pet."""
    db_pet = pet_service.get_pet(db, pet_id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_pet.cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para atualizar este pet")

    return pet_service.update_pet(db=db, pet=db_pet, updates=pet_in)


@admin_router.delete("/{pet_id}", status_code=status.HTTP_200_OK, tags=["Pets Admin"])
def delete_pet(
    pet_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):
    """Deleta um pet. Clientes não podem deletar pets com atendimentos vinculados."""
    db_pet = pet_service.get_pet(db, pet_id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet não encontrado")

    # Verifica se o usuário tem permissão para deletar
    is_owner = db_pet.cliente.cpf == current_user.cpf
    is_admin = current_user.perfil == models.PerfilUsuario.ADMIN

    if not is_owner and not is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Não tem permissão para deletar este pet")

    # Regra de negócio: Apenas admins podem deletar pets com atendimentos
    if not is_admin:
        atendimentos = atendimento_service.get_atendimentos_by_pet(db=db, pet_id=pet_id)
        if atendimentos:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Este pet possui atendimentos e não pode ser excluído. Contate um administrador."
            )

    pet_service.delete_pet(db=db, pet=db_pet)
    return {"detail": "Pet deletado com sucesso"}
