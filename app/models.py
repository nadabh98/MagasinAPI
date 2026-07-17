from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from .database import Base


class Client(Base):
    __tablename__ = "clients"

    id_client = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String(50), nullable=True)
    ville = Column(String(50), nullable=True)


class Commande(Base):
    __tablename__ = "commandes"

    id_commande = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_client = Column(Integer, ForeignKey("clients.id_client"), nullable=True)
    produit = Column(String(50), nullable=True)
    montant = Column(Numeric(8, 2), nullable=True)
