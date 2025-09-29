from pydantic import BaseModel
from app.models.models import TipoContato

class ContatoBase(BaseModel):
    tag: str | None = None
    tipo: TipoContato
    valor: str


class ContatoCreate(ContatoBase):
    pass


class ContatoUpdate(BaseModel):
    tag: str | None = None
    tipo: TipoContato | None = None
    valor: str | None = None


class ContatoInDBBase(ContatoBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True


class Contato(ContatoInDBBase):
    pass
