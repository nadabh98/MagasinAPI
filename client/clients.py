import tkinter as tk
from tkinter import ttk, messagebox

from client.api import get_clients, ajouter_client


class FenetreClients(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Gestion des clients")
        self.geometry("600x400")

        self.creer_formulaire()
        self.creer_tableau()

        self.charger_clients()


    def creer_formulaire(self):

        cadre = tk.Frame(self, padx=10, pady=10)
        cadre.pack(fill="x")


        tk.Label(cadre, text="Nom").grid(row=0, column=0)
        tk.Label(cadre, text="Ville").grid(row=0, column=1)


        self.nom = tk.Entry(cadre, width=20)
        self.ville = tk.Entry(cadre, width=20)


        self.nom.grid(row=1, column=0, padx=5)
        self.ville.grid(row=1, column=1, padx=5)


        bouton = tk.Button(
            cadre,
            text="Ajouter client",
            command=self.ajouter
        )

        bouton.grid(row=1, column=2, padx=10)



    def creer_tableau(self):

        colonnes = (
            "id_client",
            "nom",
            "ville"
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
                width=150
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
            command=self.charger_clients
        )

        bouton.pack()



    def charger_clients(self):

        for ligne in self.tableau.get_children():
            self.tableau.delete(ligne)


        try:

            clients = get_clients()

            for client in clients:

                self.tableau.insert(
                    "",
                    "end",
                    values=(
                        client["id_client"],
                        client["nom"],
                        client["ville"]
                    )
                )


        except Exception as erreur:

            messagebox.showerror(
                "Erreur",
                str(erreur)
            )



    def ajouter(self):

        try:

            ajouter_client(
                self.nom.get(),
                self.ville.get()
            )


            messagebox.showinfo(
                "Succès",
                "Client ajouté"
            )


            self.charger_clients()


        except Exception as erreur:

            messagebox.showerror(
                "Erreur",
                str(erreur)
            )
