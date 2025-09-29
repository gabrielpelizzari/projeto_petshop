import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import raca_service
from app.schemas.raca import RacaCreate

# Lista de raças para popular o banco
RACAS_PARA_CADASTRAR = [
    "Shih Tzu",
    "Golden Retriever",
    "Buldogue Francês",
    "Lulu da Pomerânia",
    "Poodle"
]

def seed_racas(db: Session):
    """Adiciona raças pré-definidas ao banco de dados se não existirem."""
    print("Iniciando o seeding de raças...")
    racas_adicionadas = 0
    for nome_raca in RACAS_PARA_CADASTRAR:
        raca_existente = raca_service.get_raca_by_nome(db, nome=nome_raca)
        if not raca_existente:
            raca_in = RacaCreate(nome=nome_raca)
            raca_service.create_raca(db=db, raca=raca_in)
            print(f"- Raça '{nome_raca}' adicionada.")
            racas_adicionadas += 1
        else:
            print(f"- Raça '{nome_raca}' já existe. Pulando.")
    
    print(f"\nSeeding concluído. {racas_adicionadas} novas raças foram adicionadas.")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_racas(db)
    finally:
        db.close()
