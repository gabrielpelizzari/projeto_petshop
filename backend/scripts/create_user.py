import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import usuario_service
from app.schemas.usuario import UsuarioCreate
from app.models.models import PerfilUsuario

def create_user(db: Session, user_in: UsuarioCreate):
    """Cria um novo usuário, verificando se o CPF já existe."""
    user_existente = usuario_service.get_usuario_by_cpf(db, cpf=user_in.cpf)
    if user_existente:
        print(f"Erro: Usuário com CPF {user_in.cpf} já existe.")
        return

    usuario = usuario_service.create_usuario(db=db, usuario=user_in)
    print(f"Usuário '{usuario.nome}' com perfil '{usuario.perfil.value}' criado com sucesso!")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        # --- CONFIGURE AQUI PARA CRIAR SEU USUÁRIO ---
        # Exemplo para criar um ADMINISTRADOR
        admin_user = UsuarioCreate(
            cpf="00000000001",
            nome="Admin Teste",
            senha="admin",
            perfil=PerfilUsuario.ADMIN
        )
        create_user(db, admin_user)

    finally:
        db.close()
