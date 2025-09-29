from pydantic import BaseModel, validator
from datetime import date

class PetBase(BaseModel):
    nome: str
    data_nascimento: date | None = None
    raca_id: int
    
    @validator('nome')
    def validate_nome(cls, v):
        """Valida se o nome do pet não está vazio."""
        if not v or not v.strip():
            raise ValueError('Nome do pet não pode estar vazio')
        return v.strip()
    
    @validator('data_nascimento')
    def validate_data_nascimento(cls, v):
        """Valida se a data de nascimento não é futura."""
        if v and v > date.today():
            raise ValueError('Data de nascimento não pode ser futura')
        return v

class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    nome: str | None = None
    data_nascimento: date | None = None
    raca_id: int | None = None
    cliente_id: int | None = None

class PetInDBBase(PetBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True

class Pet(PetInDBBase):
    pass
