from sqlalchemy.orm import Session
from app.models import models
from app.schemas import cliente as cliente_schema


def get_cliente(db: Session, cliente_id: int) -> models.Cliente | None:
    """Busca um cliente pelo ID."""
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()


def get_cliente_by_cpf(db: Session, cpf: str) -> models.Cliente | None:
    """Busca um cliente pelo CPF."""
    return db.query(models.Cliente).filter(models.Cliente.cpf == cpf).first()


def get_clientes(db: Session, skip: int = 0, limit: int = 100) -> list[dict]:
    """Lista todos os clientes com seus perfis de usuário."""
    clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
    clientes_com_perfil = []
    for cliente in clientes:
        cliente_dict = cliente.__dict__
        cliente_dict['perfil'] = cliente.usuario.perfil
        clientes_com_perfil.append(cliente_dict)
    return clientes_com_perfil


def update_cliente(
    db: Session, 
    cliente: models.Cliente, 
    updates: cliente_schema.ClienteUpdate) -> models.Cliente:
    """Atualiza os dados de um cliente."""
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cliente, key, value)
    
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente
