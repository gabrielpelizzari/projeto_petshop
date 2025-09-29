from pydantic import BaseModel

class RacaBase(BaseModel):
    nome: str

class RacaCreate(RacaBase):
    pass

class RacaUpdate(RacaBase):
    pass

class RacaInDBBase(RacaBase):
    id: int

    class Config:
        from_attributes = True

class Raca(RacaInDBBase):
    pass
