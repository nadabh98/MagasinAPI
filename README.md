# 🏪 MagasinAP# 🏪 MagasinAPI

Projet complet de gestion d'un magasin développé avec **Python**, comprenant :

- une API REST développée avec **FastAPI**
- une base de données **MySQL (FreeDB)**
- une application cliente graphique développée avec **Tkinter**
- un déploiement cloud avec **Render**

---

# 🎯 Objectif du projet

Créer une application permettant de gérer :

- les clients d'un magasin
- les commandes associées aux clients

L'application utilise une architecture client / serveur :

Utilisateur
|
↓
Interface graphique Tkinter
|
↓ HTTP Requests
|
API FastAPI
|
↓ SQLAlchemy
|
Base MySQL FreeDB

---

## 🚀 Fonctionnalités

### API FastAPI

- Gestion des clients
- Gestion des commandes
- Création automatique des tables via SQLAlchemy
- Documentation interactive Swagger

### # 🖥️ Application graphique Tkinter

L'application cliente permet :

## Gestion des clients

- afficher les clients
- ajouter un client
- actualiser la liste


## Gestion des commandes

- afficher les commandes
- ajouter une commande
- associer une commande à un client


---

## 🏗️ Architecture du projet

MagasinAPI/

│
├── app/ # API FastAPI
│
│ ├── main.py # Routes API
│ ├── database.py # Connexion base de données
│ ├── models.py # Modèles SQLAlchemy
│ └── schemas.py # Schémas Pydantic
│
├── client/ # Application Tkinter
│
│ ├── app.py # Menu principal
│ ├── clients.py # Interface clients
│ ├── commandes.py # Interface commandes
│ └── api.py # Communication avec FastAPI
│
├── requirements.txt
├── render.yaml
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
