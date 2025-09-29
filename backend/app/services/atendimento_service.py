from sqlalchemy.orm import Session
from app.models import models
from app.schemas import atendimento as atendimento_schema

def get_atendimento(db: Session, atendimento_id: int) -> models.Atendimento | None:
    """Busca um atendimento pelo ID."""
    return db.query(models.Atendimento).filter(models.Atendimento.id == atendimento_id).first()


def get_atendimentos_by_pet(db: Session, pet_id: int, skip: int = 0, limit: int = 100) -> list[models.Atendimento]:
    """Lista os atendimentos de um pet específico."""
    return db.query(models.Atendimento).filter(models.Atendimento.pet_id == pet_id).offset(skip).limit(limit).all()


def get_all_atendimentos_with_relations(
    db: Session,
    skip: int = 0,
    limit: int = 100) -> list[tuple[models.Atendimento, models.Pet, models.Cliente]]:

    """Retorna atendimentos com dados do pet e cliente associados."""
    query = (
        db.query(models.Atendimento, models.Pet, models.Cliente)
        .join(models.Pet, models.Atendimento.pet_id == models.Pet.id)
        .join(models.Cliente, models.Pet.cliente_id == models.Cliente.id)
        .offset(skip)
        .limit(limit)
    )
    return query.all()


def create_atendimento_for_pet(
    db: Session, atendimento: atendimento_schema.AtendimentoCreate, pet_id: int) -> models.Atendimento:

    """Cria um novo atendimento para um pet."""
    db_atendimento = models.Atendimento(
        descricao=atendimento.descricao,
        valor=atendimento.valor,
        data=atendimento.data,
        pet_id=pet_id
    )
    db.add(db_atendimento)
    db.commit()
    db.refresh(db_atendimento)
    return db_atendimento


def update_atendimento(
    db: Session, 
    atendimento: models.Atendimento, 
    updates: atendimento_schema.AtendimentoUpdate) -> models.Atendimento:

    """Atualiza os dados de um atendimento."""
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(atendimento, key, value)
    
    db.add(atendimento)
    db.commit()
    db.refresh(atendimento)
    return atendimento


def delete_atendimento(db: Session, atendimento: models.Atendimento):
    """Deleta um atendimento do banco de dados."""
    db.delete(atendimento)
    db.commit()
