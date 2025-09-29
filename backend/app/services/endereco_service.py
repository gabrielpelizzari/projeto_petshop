from sqlalchemy.orm import Session
from app.models import models
from app.schemas import endereco as endereco_schema


def create_endereco_for_cliente(
    db: Session, endereco: endereco_schema.EnderecoCreate, cliente_id: int) -> models.Endereco:
    """Cria um novo endereço para um cliente."""
    db_endereco = models.Endereco(**endereco.model_dump(), cliente_id=cliente_id)
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco


def get_endereco(db: Session, endereco_id: int) -> models.Endereco | None:
    """Busca um endereço pelo ID."""
    return db.query(models.Endereco).filter(models.Endereco.id == endereco_id).first()


def update_endereco(
    db: Session, 
    endereco: models.Endereco, 
    updates: endereco_schema.EnderecoUpdate) -> models.Endereco:
    """Atualiza os dados de um endereço."""
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(endereco, key, value)
    
    db.add(endereco)
    db.commit()
    db.refresh(endereco)
    return endereco


def delete_endereco(db: Session, endereco: models.Endereco):
    """Deleta um endereço do banco de dados."""
    db.delete(endereco)
    db.commit()
