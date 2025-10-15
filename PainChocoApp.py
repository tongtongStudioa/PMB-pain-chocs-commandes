import customtkinter as ctk
from tkinter import messagebox
import datetime
from affiche_infos_utiles import generer_rapport
from main import horaires_pauses
from main import listes_classes

# --- Simulation de ta logique principale (à remplacer par ton code réel) ---
def lancer_analyse(classes):
    if not classes:
        return "❌ Aucune classe ajoutée."
    # Exemple fictif : simule un traitement et création PDF
    resultats = [f"{c['nom']} ({c['effectif']} étudiants)" for c in classes]
    return f"✅ PDF généré pour : " + ", ".join(resultats)

# --- Application ---
class PainChocoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pain au Chocolat Planner 🍫🥐")
        self.geometry("700x500")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.classes = []  # stockage des classes ajoutées

        # ======== SECTION FORMULAIRE ========
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(pady=10, padx=10, fill="x")

        self.entry_nom = ctk.CTkEntry(frame_form, placeholder_text="Nom de la classe")
        self.entry_nom.pack(side="left", padx=5, pady=5, expand=True)

        self.entry_nb = ctk.CTkEntry(frame_form, placeholder_text="Nombre d'étudiants")
        self.entry_nb.pack(side="left", padx=5, pady=5, expand=True)

        self.entry_url = ctk.CTkEntry(frame_form, placeholder_text="URL Hyperplanning")
        self.entry_url.pack(side="left", padx=5, pady=5, expand=True)

        bouton_add = ctk.CTkButton(frame_form, text="Ajouter", command=self.ajouter_classe)
        bouton_add.pack(side="left", padx=5, pady=5)

        # ======== SECTION LISTE ========
        frame_list = ctk.CTkFrame(self)
        frame_list.pack(pady=10, padx=10, fill="both", expand=True)

        self.listbox = ctk.CTkTextbox(frame_list, wrap="none")
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.listbox.insert("end", "📋 Aucune classe ajoutée pour le moment.\n")
        self.listbox.configure(state="disabled")

        # ======== NOM DU RAPPORT ========
        frame_rapport = ctk.CTkFrame(self)
        frame_rapport.pack(pady=5, padx=10, fill="x")

        label_rapport = ctk.CTkLabel(frame_rapport, text="Nom du rapport :")
        label_rapport.pack(side="left", padx=5)

        self.entry_rapport = ctk.CTkEntry(frame_rapport, placeholder_text="ex: PMB planning jan - juin 2026")
        self.entry_rapport.pack(side="left", padx=5, fill="x", expand=True)

        # ======== SECTION ACTION ========
        frame_action = ctk.CTkFrame(self)
        frame_action.pack(pady=10, padx=10, fill="x")

        bouton_run = ctk.CTkButton(frame_action, text="Lancer l'analyse", command=self.lancer_programme)
        bouton_run.pack(side="left", padx=10)

        bouton_clear = ctk.CTkButton(frame_action, text="Vider la liste", fg_color="red", command=self.confirm_clear)
        bouton_clear.pack(side="left", padx=10)

        # ======== SECTION LOGS ========
        frame_logs = ctk.CTkFrame(self)
        frame_logs.pack(pady=10, padx=10, fill="both", expand=True)

        self.logs = ctk.CTkTextbox(frame_logs)
        self.logs.pack(fill="both", expand=True, padx=5, pady=5)
        self.log("🟡 Application démarrée.")

    def ajouter_classe(self):
        nom = self.entry_nom.get().strip()
        nb = self.entry_nb.get().strip()
        url = self.entry_url.get().strip()

        if not nom or not nb or not url:
            self.log("❌ Tous les champs sont obligatoires.")
            return

        if not nb.isdigit():
            self.log(f"❌ Nombre invalide pour {nom}.")
            return

        self.classes.append({"nom": nom, "effectif": int(nb), "url_edt": url})
        self.mettre_a_jour_liste()
        self.log(f"✅ Classe ajoutée : {nom} ({nb} étudiants)")

        # vider les champs
        self.entry_nom.delete(0, "end")
        self.entry_nb.delete(0, "end")
        self.entry_url.delete(0, "end")

    def mettre_a_jour_liste(self):
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0", "end")
        if not self.classes:
            self.listbox.insert("end", "📋 Aucune classe ajoutée pour le moment.\n")
        else:
            for c in self.classes:
                self.listbox.insert("end", f"• {c['nom']} — {c['effectif']} étudiants — {c['url_edt']}\n")
        self.listbox.configure(state="disabled")

    def clear_classes(self):
        self.classes.clear()
        self.mettre_a_jour_liste()
        self.log("🧹 Liste des classes vidée.")

    def confirm_clear(self):
        if messagebox.askyesno("Confirmation", "⚠️ Voulez-vous vraiment vider la liste des classes ?"):
            self.clear_classes()

    def lancer_programme(self):
        nom_rapport = self.entry_rapport.get().strip()
        msg = generer_rapport(horaires_pauses, self.classes, nom_rapport)
        self.log(msg)
        messagebox.showinfo("Résultat", msg)

    def log(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.logs.insert("end", f"[{now}] {message}\n")
        self.logs.see("end")

if __name__ == "__main__":
    app = PainChocoApp()
    app.mainloop()
