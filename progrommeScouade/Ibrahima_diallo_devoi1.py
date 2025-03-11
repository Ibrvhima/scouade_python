import tkinter as tk
from tkinter import messagebox

NAME = "Ibrahima Diallo"  

class SimpleApp:
    """
    Classe SimpleApp pour créer une application simple avec Tkinter
    """
    def __init__(self, root: tk.Tk) -> None:
        """
        Constructeur de la classe SimpleApp

        :param root: Fenêtre principale de l'application
        :type root: BaseWidget (tk.Tk)
        """
        self.root = root
        self.root.title("Hello World")
        self.root.geometry("300x200")
        
        # Message de bienvenue
        self.label = tk.Label(root, text=f"Bienvenue {NAME} !!!", font=('Arial', 12))
        self.label.pack(pady=30)
        
        # Bouton Quitter
        self.quit_button = tk.Button(root, text="Quitter", command=self.confirm_quit)
        self.quit_button.pack()
    
    def confirm_quit(self) -> None:
        """
        Méthode pour confirmer la fermeture de l'application
        """
        if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()