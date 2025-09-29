from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core import security
from app.core.database import get_db
from app.schemas import token
from app.services import usuario_service

router = APIRouter()

@router.post("/login", response_model=token.Token, tags=["Autenticação"])
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Autentica o usuário e retorna um token de acesso."""
    usuario = usuario_service.authenticate_usuario(
        db, cpf=form_data.username, senha=form_data.password
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="CPF ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=usuario.cpf, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
