from pydantic import BaseModel, validator
from datetime import date

class AtendimentoBase(BaseModel):
    descricao: str
    valor: float
    data: date
    
    @validator('descricao')
    def validate_descricao(cls, v):
        """Valida se a descrição não está vazia."""
        if not v or not v.strip():
            raise ValueError('Descrição do atendimento não pode estar vazia')
        return v.strip()
    
    @validator('valor')
    def validate_valor(cls, v):
        """Valida se o valor é positivo."""
        if v <= 0:
            raise ValueError('Valor do atendimento deve ser positivo')
        return v


class AtendimentoCreate(AtendimentoBase):
    pass


class AtendimentoUpdate(BaseModel):
    descricao: str | None = None
    valor: float | None = None
    data: date | None = None


class AtendimentoInDBBase(AtendimentoBase):
    id: int
    pet_id: int

    class Config:
        from_attributes = True


class Atendimento(AtendimentoInDBBase):
    pass


class AtendimentoAdminResponse(Atendimento):
    pet_nome: str
    cliente_id: int
    cliente_nome: str
