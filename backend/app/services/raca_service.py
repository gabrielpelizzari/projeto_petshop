from sqlalchemy.orm import Session
from app.models import models
from app.schemas import raca as raca_schema


def get_raca(db: Session, raca_id: int) -> models.Raca | None:
    """Busca uma raça pelo ID."""
    return db.query(models.Raca).filter(models.Raca.id == raca_id).first()


def get_raca_by_descricao(db: Session, descricao: str) -> models.Raca | None:
    """Busca uma raça pela descrição (nome)."""
    return db.query(models.Raca).filter(models.Raca.nome == descricao).first()


def get_racas(db: Session, skip: int = 0, limit: int = 100) -> list[models.Raca]:
    """Lista todas as raças."""
    return db.query(models.Raca).offset(skip).limit(limit).all()


def get_raca_by_nome(db: Session, nome: str) -> models.Raca | None:
    """Busca uma raça pelo nome."""
    return db.query(models.Raca).filter(models.Raca.nome == nome).first()


def create_raca(db: Session, raca: raca_schema.RacaCreate) -> models.Raca:
    """Cria uma nova raça no banco de dados."""
    db_raca = models.Raca(nome=raca.nome)
    db.add(db_raca)
    db.commit()
    db.refresh(db_raca)
    return db_raca


def update_raca(db: Session, db_raca: models.Raca, raca_update: raca_schema.RacaUpdate) -> models.Raca:
    """Atualiza uma raça no banco de dados."""
    db_raca.nome = raca_update.nome
    db.commit()
    db.refresh(db_raca)
    return db_raca


def delete_raca(db: Session, raca: models.Raca):
    """Deleta uma raça do banco de dados."""
    db.delete(raca)
    db.commit()
