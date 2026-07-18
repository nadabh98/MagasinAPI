from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models, schemas


# ---------------------------------------
# Création des tables dans la base
# ---------------------------------------
Base.metadata.create_all(bind=engine)


# ---------------------------------------
# Création de l'application FastAPI
# ---------------------------------------
app = FastAPI(
    title="Magasin API",
    description="API de gestion d'un magasin",
    version="1.0"
)


# ==========================================================
#                       CLIENTS
# ==========================================================

# Lire tous les clients
@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()


# Ajouter un client
@app.post("/clients")
def create_client(client: schemas.ClientCreate,
                  db: Session = Depends(get_db)):

    nouveau_client = models.Client(
        nom=client.nom,
        ville=client.ville
    )

    db.add(nouveau_client)
    db.commit()
    db.refresh(nouveau_client)

    return nouveau_client


# Modifier un client
@app.put("/clients/{id_client}")
def update_client(id_client: int,
                  client: schemas.ClientUpdate,
                  db: Session = Depends(get_db)):

    client_db = db.query(models.Client).filter(
        models.Client.id_client == id_client
    ).first()

    # Vérifie si le client existe
    if client_db is None:
        raise HTTPException(
            status_code=404,
            detail="Client introuvable"
        )

    # Mise à jour des informations
    client_db.nom = client.nom
    client_db.ville = client.ville

    db.commit()
    db.refresh(client_db)

    return client_db


# Supprimer un client
@app.delete("/clients/{id_client}")
def delete_client(id_client: int,
                  db: Session = Depends(get_db)):

    client_db = db.query(models.Client).filter(
        models.Client.id_client == id_client
    ).first()

    if client_db is None:
        raise HTTPException(
            status_code=404,
            detail="Client introuvable"
        )

    db.delete(client_db)
    db.commit()

    return {
        "message": "Client supprimé avec succès"
    }


# ==========================================================
#                      COMMANDES
# ==========================================================

# Lire toutes les commandes
@app.get("/commandes")
def get_commandes(db: Session = Depends(get_db)):
    return db.query(models.Commande).all()


# Ajouter une commande
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


# Modifier une commande
@app.put("/commandes/{id_commande}")
def update_commande(
        id_commande: int,
        commande: schemas.CommandeUpdate,
        db: Session = Depends(get_db)
):

    commande_db = db.query(models.Commande).filter(
        models.Commande.id_commande == id_commande
    ).first()

    if commande_db is None:
        raise HTTPException(
            status_code=404,
            detail="Commande introuvable"
        )

    commande_db.id_client = commande.id_client
    commande_db.produit = commande.produit
    commande_db.montant = commande.montant

    db.commit()
    db.refresh(commande_db)

    return commande_db


# Supprimer une commande
@app.delete("/commandes/{id_commande}")
def delete_commande(
        id_commande: int,
        db: Session = Depends(get_db)
):

    commande_db = db.query(models.Commande).filter(
        models.Commande.id_commande == id_commande
    ).first()

    if commande_db is None:
        raise HTTPException(
            status_code=404,
            detail="Commande introuvable"
        )

    db.delete(commande_db)
    db.commit()

    return {
        "message": "Commande supprimée avec succès"
    }


# ==========================================================
#                  PAGE D'ACCUEIL
# ==========================================================

@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur l'API Magasin"
    }
