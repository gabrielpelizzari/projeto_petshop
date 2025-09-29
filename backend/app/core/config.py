from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configurações do Banco de Dados MySQL
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "petshop_user"
    DB_PASSWORD: str = "petshop_password"
    DB_NAME: str = "petshop_db"
    
    # Configurações de Segurança
    SECRET_KEY: str = "your-secret-key-change-in-production" # Alterar em produção
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MAX_LOGIN_ATTEMPTS: int = 5
    LOGIN_ATTEMPT_TIMEOUT: int = 900
    
    # Configurações da Aplicação
    DEBUG: bool = True
    ENVIRONMENT: str = "development"

    @property
    def DATABASE_URL(self) -> str:
        """Constrói a URL do banco de dados MySQL."""
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
