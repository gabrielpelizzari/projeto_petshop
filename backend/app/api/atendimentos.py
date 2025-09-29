from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import atendimento as atendimento_schema
from app.services import atendimento_service, pet_service
from app.api import deps
from app.models import models

router = APIRouter()


@router.get("/atendimentos", response_model=list[atendimento_schema.AtendimentoAdminResponse], tags=["Atendimentos"])
def read_all_atendimentos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.Usuario = Depends(deps.get_current_active_admin)
):
    """Lista todos os atendimentos com dados do pet e do cliente. Acesso restrito a administradores."""
    registros = atendimento_service.get_all_atendimentos_with_relations(db, skip=skip, limit=limit)
    respostas: list[atendimento_schema.AtendimentoAdminResponse] = []
    for atendimento, pet, cliente in registros:
        respostas.append(
            atendimento_schema.AtendimentoAdminResponse(
                id=atendimento.id,
                descricao=atendimento.descricao,
                valor=atendimento.valor,
                data=atendimento.data,
                pet_id=pet.id,
                pet_nome=pet.nome,
                cliente_id=cliente.id,
                cliente_nome=cliente.nome,
            )
        )
    return respostas


@router.post("/pets/{pet_id}/atendimentos", response_model=atendimento_schema.Atendimento, tags=["Atendimentos"])
def create_atendimento(
    pet_id: int,
    atendimento_in: atendimento_schema.AtendimentoCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)
):
    """Cria um novo atendimento para um pet. Acesso restrito a administradores."""
    db_pet = pet_service.get_pet(db, pet_id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    return atendimento_service.create_atendimento_for_pet(db=db, atendimento=atendimento_in, pet_id=pet_id)


@router.get("/pets/{pet_id}/atendimentos", response_model=list[atendimento_schema.Atendimento], tags=["Atendimentos"])
def read_atendimentos_from_pet(
    pet_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)
):
    """Lista os atendimentos de um pet."""
    db_pet = pet_service.get_pet(db, pet_id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    if current_user.perfil != models.PerfilUsuario.ADMIN and db_pet.cliente.cpf != current_user.cpf:
        raise HTTPException(status_code=403, detail="Não tem permissão para ver os atendimentos deste pet")

    return atendimento_service.get_atendimentos_by_pet(db=db, pet_id=pet_id)


@router.put("/atendimentos/{atendimento_id}", response_model=atendimento_schema.Atendimento, tags=["Atendimentos"])
def update_atendimento(
    atendimento_id: int,
    atendimento_in: atendimento_schema.AtendimentoUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)
):
    """Atualiza um atendimento. Acesso restrito a administradores."""
    db_atendimento = atendimento_service.get_atendimento(db, atendimento_id=atendimento_id)
    if not db_atendimento:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")

    return atendimento_service.update_atendimento(db=db, atendimento=db_atendimento, updates=atendimento_in)


@router.delete("/atendimentos/{atendimento_id}", status_code=status.HTTP_200_OK, tags=["Atendimentos"])
def delete_atendimento(
    atendimento_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)
):
    """Deleta um atendimento. Acesso restrito a administradores."""
    db_atendimento = atendimento_service.get_atendimento(db, atendimento_id=atendimento_id)
    if not db_atendimento:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")

    atendimento_service.delete_atendimento(db=db, atendimento=db_atendimento)
    return {"detail": "Atendimento deletado com sucesso"}
