from pydantic import BaseModel
from decimal import Decimal


# Schema pour créer un client
class ClientCreate(BaseModel):
    nom: str | None = None
    ville: str | None = None


# Schema pour afficher un client
class Client(ClientCreate):
    id_client: int

    class Config:
        from_attributes = True



# Schema pour créer une commande
class CommandeCreate(BaseModel):
    id_client: int | None = None
    produit: str | None = None
    montant: Decimal | None = None


# Schema pour afficher une commande
class Commande(CommandeCreate):
    id_commande: int

    class Config:
        from_attributes = True
