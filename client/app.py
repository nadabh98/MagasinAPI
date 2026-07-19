import tkinter as tk
from tkinter import ttk, messagebox

from api import get_clients, ajouter_client


class ApplicationMagasin(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Gestion du Magasin - Client FastAPI")
        self.geometry("800x500")

        self.creer_formulaire()
        self.creer_tableau()

        #self.charger_clients()


    # -----------------------------
    # Formulaire client
    # -----------------------------

    def creer_formulaire(self):

        cadre = tk.Frame(self, padx=10, pady=10)
        cadre.pack(fill="x")


        tk.Label(cadre, text="Nom :").grid(row=0, column=0)

        self.champ_nom = tk.Entry(cadre)
        self.champ_nom.grid(row=0, column=1, padx=5)


        tk.Label(cadre, text="Ville :").grid(row=0, column=2)

        self.champ_ville = tk.Entry(cadre)
        self.champ_ville.grid(row=0, column=3, padx=5)


        bouton = tk.Button(
            cadre,
            text="Ajouter Client",
            command=self.ajouter_client
        )

        bouton.grid(row=0, column=4, padx=10)



    # -----------------------------
    # Tableau clients
    # -----------------------------

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



    # -----------------------------
    # Charger les clients depuis API
    # -----------------------------

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
                "Erreur API",
                str(erreur)
            )



    # -----------------------------
    # Ajouter un client
    # -----------------------------

    def ajouter_client(self):

        nom = self.champ_nom.get()
        ville = self.champ_ville.get()


        if not nom:

            messagebox.showwarning(
                "Attention",
                "Le nom est obligatoire"
            )

            return


        try:

            ajouter_client(
                nom,
                ville
            )


            messagebox.showinfo(
                "Succès",
                "Client ajouté"
            )


            self.charger_clients()


            self.champ_nom.delete(0, tk.END)
            self.champ_ville.delete(0, tk.END)


        except Exception as erreur:

            messagebox.showerror(
                "Erreur",
                str(erreur)
            )



if __name__ == "__main__":

    application = ApplicationMagasin()

    application.mainloop()
