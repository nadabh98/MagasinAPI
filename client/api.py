import requests

# URL  API Render
URL_BASE = "https://magasinapi.onrender.com"

# -------------------------
# Clients
# -------------------------


def get_clients():
    reponse = requests.get(f"{URL_BASE}/clients")
    reponse.raise_for_status()
    return reponse.json()


def ajouter_client(nom, ville):

    donnees = {
        "nom": nom,
        "ville": ville
    }

    reponse = requests.post(
        f"{URL_BASE}/clients",
        json=donnees
    )

    reponse.raise_for_status()

    return reponse.json()


def supprimer_client(id_client):

    reponse = requests.delete(
        f"{URL_BASE}/clients/{id_client}"
    )

    reponse.raise_for_status()

    return reponse.json()

# -------------------------
# Commandes
# -------------------------

def get_commandes():
    response = requests.get(f"{URL_BASE}/commandes")
    response.raise_for_status()
    return response.json()


def ajouter_commande(id_client, produit, montant):

    donnees = {
        "id_client": id_client,
        "produit": produit,
        "montant": montant
    }

    response = requests.post(
        f"{URL_BASE}/commandes",
        json=donnees
    )

    response.raise_for_status()

    return response.json()
