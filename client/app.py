# Import de la bibliothèque tkinter pour créer l'interface graphique
import tkinter as tk


# Import des deux fenêtres de gestion
# FenetreClients : interface pour gérer les clients
# FenetreCommandes : interface pour gérer les commandes
from client.clients import FenetreClients
from client.commandes import FenetreCommandes



# Création de la fenêtre principale de l'application
# tk.Tk représente la fenêtre principale d'un programme Tkinter
class ApplicationMagasin(tk.Tk):


    # Constructeur de la classe
    # Cette fonction est exécutée automatiquement lors de la création de l'application
    def __init__(self):

        # Appel du constructeur de la classe parent tk.Tk
        # Permet d'initialiser correctement la fenêtre Tkinter
        super().__init__()


        # Définition du titre affiché en haut de la fenêtre
        self.title("Magasin API - Gestion")


        # Définition de la taille de la fenêtre
        # largeur x hauteur
        self.geometry("400x300")


        # Création de l'interface graphique
        self.creer_interface()



    # Fonction responsable de la création des éléments graphiques
    # (labels, boutons...)
    def creer_interface(self):


        # Création d'un titre dans la fenêtre
        titre = tk.Label(
            self,
            text="Gestion du magasin",
            font=("Arial", 18)
        )


        # Placement du titre dans la fenêtre
        # pady ajoute un espace vertical autour du composant
        titre.pack(pady=30)



        # Création du bouton permettant d'ouvrir la gestion des clients
        bouton_clients = tk.Button(
            self,

            # Texte affiché sur le bouton
            text="Gestion des clients",

            # Largeur du bouton
            width=25,

            # Hauteur du bouton
            height=2,

            # Fonction appelée quand l'utilisateur clique sur le bouton
            command=self.ouvrir_clients
        )


        # Placement du bouton dans la fenêtre
        bouton_clients.pack(pady=10)



        # Création du bouton permettant d'ouvrir la gestion des commandes
        bouton_commandes = tk.Button(
            self,

            # Texte affiché sur le bouton
            text="Gestion des commandes",

            width=25,

            height=2,

            # Appelle la fonction ouvrir_commandes au clic
            command=self.ouvrir_commandes
        )


        # Placement du bouton commandes
        bouton_commandes.pack(pady=10)





    # Fonction appelée lorsque l'utilisateur clique sur
    # "Gestion des clients"
    def ouvrir_clients(self):

        # Création d'une nouvelle fenêtre client
        # self représente la fenêtre principale comme parent
        FenetreClients(self)




    # Fonction appelée lorsque l'utilisateur clique sur
    # "Gestion des commandes"
    def ouvrir_commandes(self):

        # Création d'une nouvelle fenêtre commandes
        FenetreCommandes(self)




# Cette condition vérifie que le fichier est exécuté directement
# et non importé par un autre fichier
if __name__ == "__main__":


    # Création de l'application principale
    application = ApplicationMagasin()


    # Lance la boucle principale Tkinter
    # Elle garde la fenêtre ouverte et attend les actions utilisateur
    application.mainloop()
