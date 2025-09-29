from sqlalchemy.orm import Session
from app.models import models
from app.schemas import contato as contato_schema

def create_contato_for_cliente(
    db: Session, contato: contato_schema.ContatoCreate, cliente_id: int) -> models.Contato:
    """Cria um novo contato para um cliente."""
    db_contato = models.Contato(**contato.model_dump(), cliente_id=cliente_id)
    db.add(db_contato)
    db.commit()
    db.refresh(db_contato)
    return db_contato


def get_contato_by_valor(db: Session, valor: str) -> models.Contato | None:
    """Busca um contato pelo seu valor (email ou telefone)."""
    return db.query(models.Contato).filter(models.Contato.valor == valor).first()


def get_contato(db: Session, contato_id: int) -> models.Contato | None:
    """Busca um contato pelo ID."""
    return db.query(models.Contato).filter(models.Contato.id == contato_id).first()


def update_contato(
    db: Session, 
    contato: models.Contato, 
    updates: contato_schema.ContatoUpdate) -> models.Contato:

    """Atualiza os dados de um contato."""
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(contato, key, value)
    
    db.add(contato)
    db.commit()
    db.refresh(contato)
    return contato


def update_or_create_principal_contato(
    db: Session, cliente_id: int, tipo: str, valor: str) -> models.Contato:

    """Atualiza o contato principal de um tipo ou o cria se não existir."""
    # Tenta encontrar um contato principal existente
    db_contato = (
        db.query(models.Contato)
        .filter(
            models.Contato.cliente_id == cliente_id,
            models.Contato.tipo == tipo,
            models.Contato.tag == 'Principal'
        )
        .first())

    if db_contato:
        # Se existe, atualiza o valor
        db_contato.valor = valor
        db.add(db_contato)
        db.commit()
        db.refresh(db_contato)
        return db_contato
    else:
        # Se não existe, cria um novo
        return create_contato_for_cliente(
            db=db,
            contato=contato_schema.ContatoCreate(tipo=tipo, valor=valor, tag='Principal'),
            cliente_id=cliente_id)


def delete_contato(db: Session, contato: models.Contato):
    """Deleta um contato do banco de dados."""
    db.delete(contato)
    db.commit()
