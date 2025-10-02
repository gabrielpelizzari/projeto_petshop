from pydantic import BaseModel, EmailStr, validator
from . import endereco as endereco_schema

class CadastroCompleto(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    senha: str
    email: EmailStr
    telefone: str
    endereco: endereco_schema.EnderecoCreate
    
    @validator('nome', 'sobrenome')
    def validate_nome_sobrenome(cls, v):
        """Valida se nome e sobrenome não estão vazios."""
        if not v or not v.strip():
            raise ValueError('Nome e sobrenome não podem estar vazios')
        return v.strip()
    
    
    @validator('cpf')
    def validate_cpf(cls, v):
        """Valida formato básico do CPF (11 dígitos)."""
        # Remove caracteres não numéricos
        cpf_limpo = ''.join(filter(str.isdigit, v))
        
        if len(cpf_limpo) != 11:
            raise ValueError('CPF deve ter exatamente 11 dígitos')
        
        # Verifica se não são todos os dígitos iguais
        if len(set(cpf_limpo)) == 1:
            raise ValueError('CPF inválido - todos os dígitos são iguais')
            
        return cpf_limpo
    

    @validator('senha')
    def validate_senha(cls, v):
        if len(v) < 8:
            raise ValueError('Senha deve ter no mínimo 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Senha deve conter letra maiúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('Senha deve conter número')
        return v
    

    @validator('telefone')
    def validate_telefone(cls, v):
        """Valida formato básico do telefone."""
        # Remove caracteres não numéricos
        telefone_limpo = ''.join(filter(str.isdigit, v))
        
        if len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
            raise ValueError('Telefone deve ter 10 ou 11 dígitos')
            
        return telefone_limpo
