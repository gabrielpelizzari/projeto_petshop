from sqlalchemy.orm import Session
from datetime import date
from app.models import models
from app.core.security import get_password_hash, verify_password
from app.schemas import usuario as usuario_schema


def create_usuario(db: Session, usuario: usuario_schema.UsuarioCreate) -> models.Usuario:
    """Cria um novo usuário no banco de dados."""
    senha_hash = get_password_hash(usuario.senha)
    db_usuario = models.Usuario(
        cpf=usuario.cpf,
        nome=usuario.nome,
        senha_hash=senha_hash,
        perfil=usuario.perfil)
    db.add(db_usuario)
    db.commit()

    # Se o usuário for um cliente, cria a entrada correspondente na tabela de clientes
    if db_usuario.perfil == models.PerfilUsuario.CLIENTE:
        db_cliente = models.Cliente(
            nome=db_usuario.nome,
            data_cadastro=date.today(),
            cpf=db_usuario.cpf)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)

    db.refresh(db_usuario)
    return db_usuario



def admin_update_usuario(
    db: Session, *, usuario: models.Usuario, updates: usuario_schema.AdminUsuarioUpdate
) -> models.Usuario:
    """Aplica atualizações a um usuário, chamado por um admin."""
    update_data = updates.model_dump(exclude_unset=True)

    if 'nome' in update_data:
        usuario.nome = update_data['nome']
        # Se o usuário também for um cliente, atualiza o nome na tabela de clientes
        if hasattr(usuario, 'cliente') and usuario.cliente:
            usuario.cliente.nome = update_data['nome']

    if 'nova_senha' in update_data and update_data['nova_senha']:
        usuario.senha_hash = get_password_hash(update_data['nova_senha'])
    
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def get_usuario_by_cpf(db: Session, cpf: str) -> models.Usuario | None:
    """Busca um usuário pelo CPF."""
    return db.query(models.Usuario).filter(models.Usuario.cpf == cpf).first()

def update_password(db: Session, *, usuario: models.Usuario, senha_antiga: str, nova_senha: str) -> bool:
    """Verifica a senha antiga e atualiza para a nova."""
    if not verify_password(senha_antiga, usuario.senha_hash):
        return False
    
    nova_senha_hash = get_password_hash(nova_senha)
    usuario.senha_hash = nova_senha_hash
    db.add(usuario)
    db.commit()
    return True

def delete_usuario(db: Session, usuario: models.Usuario):
    """Deleta um usuário do banco de dados."""
    db.delete(usuario)
    db.commit()


def authenticate_usuario(db: Session, cpf: str, senha: str) -> models.Usuario | None:
    """Autentica um usuário, verificando CPF e senha."""
    usuario = get_usuario_by_cpf(db, cpf=cpf)
    if not usuario:
        return None
    if not verify_password(senha, usuario.senha_hash):
        return None
    return usuario
