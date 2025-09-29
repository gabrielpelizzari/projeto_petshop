from pydantic import BaseModel

class EnderecoBase(BaseModel):
    logradouro: str
    cidade: str
    bairro: str
    complemento: str | None = None
    tag: str | None = None


class EnderecoCreate(EnderecoBase):
    pass


class EnderecoUpdate(BaseModel):
    logradouro: str | None = None
    cidade: str | None = None
    bairro: str | None = None
    complemento: str | None = None
    tag: str | None = None

class EnderecoInDBBase(EnderecoBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True

class Endereco(EnderecoInDBBase):
    pass
