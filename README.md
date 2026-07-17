# 🛒 MagasinAPI - FastAPI REST API

## 📌 Description

MagasinAPI est une API REST développée avec **FastAPI** permettant de gérer les clients et les commandes d'un magasin.

Le projet met en œuvre une architecture backend moderne avec :
- FastAPI pour la création des services web
- SQLAlchemy pour l'accès aux données
- MySQL/MariaDB pour la base de données
- Pydantic pour la validation des données
- Déploiement prévu sur Render avec une base MySQL distante

---

# 🚀 Fonctionnalités

## Gestion des clients

- Création d'un client
- Consultation de la liste des clients

## Gestion des commandes

- Création d'une commande
- Consultation des commandes

---

# 🏗️ Architecture du projet

MagasinAPI/
│
├── app/
│ ├── main.py # Point d'entrée FastAPI
│ ├── database.py # Connexion SQLAlchemy
│ ├── models.py # Modèles des tables
│ ├── schemas.py # Validation Pydantic
│ └── init.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env # Variables d'environnement (non versionné)

---

# 🛠️ Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage principal |
| FastAPI | Framework API REST |
| SQLAlchemy | ORM base de données |
| MySQL/MariaDB | Base de données |
| Pydantic | Validation des données |
| Uvicorn | Serveur ASGI |
| Git/GitHub | Versionnement |

---

# ⚙️ Installation locale

## 1. Cloner le projet

```bash
git clone https://github.com/nadabh98/MagasinAPI.git
