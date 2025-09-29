from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.core import security
from app.core.config import settings
from app.core.database import get_db
from app.models import models
from app.schemas import token as token_schema
from app.services import usuario_service

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/login"
)

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)) -> models.Usuario:
    """Dependência para obter o usuário atual a partir do token JWT."""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = token_schema.TokenData(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"})
    
    if token_data.sub is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido (subject não encontrado)",
            headers={"WWW-Authenticate": "Bearer"})

    user = usuario_service.get_usuario_by_cpf(db, cpf=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuário não encontrado")
    return user


def get_current_active_admin(current_user: models.Usuario = Depends(get_current_user)) -> models.Usuario:
    """Dependência para obter o usuário atual e verificar se ele é um admin."""
    if current_user.perfil != models.PerfilUsuario.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="O usuário não tem privilégios suficientes")
    return current_user
