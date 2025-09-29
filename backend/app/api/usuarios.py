from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import usuario as usuario_schema
from app.services import usuario_service
from app.api import deps
from app.models import models

router = APIRouter()

@router.post(
    "/", 
    response_model=usuario_schema.Usuario,
    status_code=status.HTTP_201_CREATED,
    tags=["Usuários"])

def create_usuario(
    usuario: usuario_schema.UsuarioCreate, 
    db: Session = Depends(get_db)):
    """Cria um novo usuário."""
    db_usuario = usuario_service.get_usuario_by_cpf(db, cpf=usuario.cpf)
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF já cadastrado."
        )
    return usuario_service.create_usuario(db=db, usuario=usuario)


@router.get("/me", response_model=usuario_schema.Usuario, tags=["Usuários"])
def read_usuario_me(
    current_user: models.Usuario = Depends(deps.get_current_user)):
    """Obtém os dados do usuário logado."""
    return current_user


@router.put("/me/update-password", tags=["Usuários"], status_code=status.HTTP_200_OK)
def update_user_password(
    password_data: usuario_schema.UsuarioUpdatePassword,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_user)):

    """Atualiza a senha do usuário logado."""
    success = usuario_service.update_password(
        db=db,
        usuario=current_user,
        senha_antiga=password_data.senha_antiga,
        nova_senha=password_data.nova_senha)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Senha antiga incorreta")

    return {"detail": "Senha atualizada com sucesso"}


@router.put("/{cpf}", response_model=usuario_schema.Usuario, tags=["Usuários"])
def admin_update_user(
    cpf: str,
    updates: usuario_schema.AdminUsuarioUpdate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_admin)):
    
    """Atualiza os dados de um usuário (nome, perfil, senha). Acesso restrito a administradores."""
    db_user = usuario_service.get_usuario_by_cpf(db, cpf=cpf)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return usuario_service.admin_update_usuario(db=db, usuario=db_user, updates=updates)
