# 🏪 MagasinAPI

API de gestion d'un magasin développée avec **FastAPI**, connectée à une base de données **MySQL (FreeDB)** et déployée sur **Render**.

Le projet contient également une application cliente graphique développée avec **Tkinter** permettant d'interagir avec l'API.

---

## 🚀 Fonctionnalités

### API FastAPI

- Gestion des clients
- Gestion des commandes
- Création automatique des tables via SQLAlchemy
- Documentation interactive Swagger

### Client Desktop Tkinter

- Affichage des clients
- Ajout de nouveaux clients
- Communication avec l'API via HTTP Requests

---

## 🏗️ Architecture du projet

MagasinAPI/
│
├── app/ # Backend FastAPI
│ ├── main.py # Routes API
│ ├── models.py # Modèles SQLAlchemy
│ ├── schemas.py # Schémas Pydantic
│ ├── database.py # Connexion base de données
│
├── client/ # Application graphique
│ ├── app.py # Interface Tkinter
│ ├── api.py # Communication avec FastAPI
│
├── requirements.txt
├── render.yaml # Configuration Render
├── README.md
└── .gitignore


---

## 🛠️ Technologies utilisées

- Python 3
- FastAPI
- SQLAlchemy
- MySQL
- FreeDB
- Tkinter
- Requests
- Git / GitHub
- Render

---

## ⚙️ Installation locale

Cloner le projet :

```bash
git clone https://github.com/nadabh98/MagasinAPI.git
