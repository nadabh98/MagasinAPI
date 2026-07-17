from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models, schemas


# Création des tables si elles n'existent pas
#Base.metadata.create_all(bind=engine)


# Création de l'application FastAPI
app = FastAPI(
    title="Magasin API",
    description="API de gestion d'un magasin",
    version="1.0"
)


# -------------------------
# Routes Clients
# -------------------------

@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return clients


@app.post("/clients")
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    nouveau_client = models.Client(
        nom=client.nom,
        ville=client.ville
    )

    db.add(nouveau_client)
    db.commit()
    db.refresh(nouveau_client)

    return nouveau_client


# -------------------------
# Routes Commandes
# -------------------------

@app.get("/commandes")
def get_commandes(db: Session = Depends(get_db)):
    commandes = db.query(models.Commande).all()
    return commandes


@app.post("/commandes")
def create_commande(
    commande: schemas.CommandeCreate,
    db: Session = Depends(get_db)
):
    nouvelle_commande = models.Commande(
        id_client=commande.id_client,
        produit=commande.produit,
        montant=commande.montant
    )

    db.add(nouvelle_commande)
    db.commit()
    db.refresh(nouvelle_commande)

    return nouvelle_commande


# Route de test
@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur l'API Magasin"
    }
