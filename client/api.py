import requests

# URL  API Render
URL_BASE = "https://magasinapi.onrender.com"


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
