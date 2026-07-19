import tkinter as tk
from tkinter import ttk, messagebox

from client.api import get_commandes, ajouter_commande


class FenetreCommandes(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Gestion des commandes")
        self.geometry("600x400")

        self.creer_formulaire()
        self.creer_tableau()

        self.charger_commandes()


    def creer_formulaire(self):

        cadre = tk.Frame(self, padx=10, pady=10)
        cadre.pack(fill="x")


        tk.Label(cadre, text="ID Client").grid(row=0, column=0)
        tk.Label(cadre, text="Produit").grid(row=0, column=1)
        tk.Label(cadre, text="Montant").grid(row=0, column=2)


        self.client = tk.Entry(cadre, width=10)
        self.produit = tk.Entry(cadre, width=20)
        self.montant = tk.Entry(cadre, width=10)


        self.client.grid(row=1, column=0, padx=5)
        self.produit.grid(row=1, column=1, padx=5)
        self.montant.grid(row=1, column=2, padx=5)


        bouton = tk.Button(
            cadre,
            text="Ajouter commande",
            command=self.ajouter
        )

        bouton.grid(row=1, column=3, padx=10)



    def creer_tableau(self):

        colonnes = (
            "id_commande",
            "id_client",
            "produit",
            "montant"
        )


        self.tableau = ttk.Treeview(
            self,
            columns=colonnes,
            show="headings"
        )


        for colonne in colonnes:

            self.tableau.heading(
                colonne,
                text=colonne
            )

            self.tableau.column(
                colonne,
                width=120
            )


        self.tableau.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )


        bouton = tk.Button(
            self,
            text="Actualiser",
            command=self.charger_commandes
        )

        bouton.pack(pady=5)



    def charger_commandes(self):

        for ligne in self.tableau.get_children():
            self.tableau.delete(ligne)


        try:

            commandes = get_commandes()


            for commande in commandes:

                self.tableau.insert(
                    "",
                    "end",
                    values=(
                        commande["id_commande"],
                        commande["id_client"],
                        commande["produit"],
                        commande["montant"]
                    )
                )


        except Exception as erreur:

            messagebox.showerror(
                "Erreur",
                str(erreur)
            )



    def ajouter(self):

        try:

            id_client = int(
                self.client.get()
            )

            montant = float(
                self.montant.get()
            )


            ajouter_commande(
                id_client,
                self.produit.get(),
                montant
            )


            messagebox.showinfo(
                "Succès",
                "Commande ajoutée"
            )


            self.charger_commandes()


        except Exception as erreur:

            messagebox.showerror(
                "Erreur",
                str(erreur)
            )
