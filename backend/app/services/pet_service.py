from sqlalchemy.orm import Session
from app.models import models
from app.schemas import pet as pet_schema

def get_pet(db: Session, pet_id: int) -> models.Pet | None:
    """Busca um pet pelo ID."""
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()


def get_all_pets(db: Session, skip: int = 0, limit: int = 100) -> list[models.Pet]:
    """Lista todos os pets do sistema."""
    return db.query(models.Pet).offset(skip).limit(limit).all()


def get_pets_by_cliente(db: Session, cliente_id: int, skip: int = 0, limit: int = 100) -> list[models.Pet]:
    """Lista os pets de um cliente específico."""
    return db.query(models.Pet).filter(models.Pet.cliente_id == cliente_id).offset(skip).limit(limit).all()


def create_pet_for_cliente(
    db: Session, pet: pet_schema.PetCreate, cliente_id: int) -> models.Pet:
    """Cria um novo pet para um cliente."""
    db_pet = models.Pet(**pet.model_dump(), cliente_id=cliente_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def update_pet(
    db: Session, 
    pet: models.Pet, 
    updates: pet_schema.PetUpdate) -> models.Pet:

    """Atualiza os dados de um pet."""
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(pet, key, value)
    
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet


def delete_pet(db: Session, pet: models.Pet):
    """Deleta um pet do banco de dados."""
    db.delete(pet)
    db.commit()
