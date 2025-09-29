from sqlalchemy import (Column, Integer, String, Date, Float, Enum as SQLEnum, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class PerfilUsuario(str, enum.Enum):
    ADMIN = "admin"
    CLIENTE = "cliente"


class TipoContato(str, enum.Enum):
    EMAIL = "email"
    TELEFONE = "telefone"


class Usuario(Base):
    __tablename__ = "usuarios"

    cpf = Column(String(11), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil = Column(SQLEnum(PerfilUsuario), nullable=False)

    cliente = relationship("Cliente", back_populates="usuario", uselist=False, cascade="all, delete-orphan")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    data_cadastro = Column(Date, nullable=False)
    cpf = Column(String(11), ForeignKey("usuarios.cpf"), unique=True, nullable=False)

    usuario = relationship("Usuario", back_populates="cliente")
    contatos = relationship("Contato", back_populates="cliente", cascade="all, delete-orphan")
    enderecos = relationship("Endereco", back_populates="cliente", cascade="all, delete-orphan")
    pets = relationship("Pet", back_populates="cliente", cascade="all, delete-orphan")


class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    tag = Column(String(50))
    tipo = Column(SQLEnum(TipoContato), nullable=False)
    valor = Column(String(100), nullable=False)

    cliente = relationship("Cliente", back_populates="contatos")


class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    logradouro = Column(String(255), nullable=False)
    cidade = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    complemento = Column(String(100))
    tag = Column(String(50))

    cliente = relationship("Cliente", back_populates="enderecos")


class Raca(Base):
    __tablename__ = "racas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False, index=True)

    pets = relationship("Pet", back_populates="raca")


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(Date)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    raca_id = Column(Integer, ForeignKey("racas.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="pets")
    raca = relationship("Raca", back_populates="pets")
    atendimentos = relationship("Atendimento", back_populates="pet", cascade="all, delete-orphan")


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)

    pet = relationship("Pet", back_populates="atendimentos")
