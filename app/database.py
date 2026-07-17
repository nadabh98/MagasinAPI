from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Charger les variables du fichier .env
load_dotenv()

# Récupérer l'URL de connexion
DATABASE_URL = os.getenv("DATABASE_URL")

# Créer la connexion avec MariaDB/MySQL
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Créer les sessions de connexion
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe de base pour les modèles SQLAlchemy
Base = declarative_base()


# Fonction utilisée par FastAPI pour ouvrir/fermer une connexion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
