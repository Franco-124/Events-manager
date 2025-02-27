import customtkinter as ctk
import threading
from models.Event import Event


"""
Aqui vamos a definir la interfaz gratica principal
permitiendo al usaurio interactuar con la aplicacion
"""
class Main_UI_retriever(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Event Manager")
        self.file_path = None
        self.files_paths = []
        self.geometry("800x400")
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Recuperar contraseña", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        self.event_title_label = ctk.CTkButton(self, text="Cerrar ventana", font=("Arial", 16, "bold"), command=self.logout)
        self.event_title_label.grid(row=0, column=1, pady=20, padx=20, sticky="ew")
    
    def logout(self):
        self.destroy()
        from UI.login import Event_manager_login
        app = Event_manager_login()
        app.mainloop()
       
        