import customtkinter as ctk
import threading
from tkinter import messagebox
from db.dbconector import Database
from UI.Interface import Main_UI


class Event_manager_login(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("Sistema de Programación de Eventos")
        self.geometry("900x900")
        self.resizable(True, True)
        
        # Configuración del tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Crear interfaz inicial
        self.create_main_frame()
        self.show_login()
    
    def create_main_frame(self):
        # Frame principal con nuevo color de fondo
        self.main_frame = ctk.CTkFrame(self, fg_color=["#f0f0f0", "#e0e0e0"])
        self.main_frame.pack(fill="both", expand=True)
        
        # Banner superior
        self.banner_frame = ctk.CTkFrame(
            self.main_frame, 
            fg_color=["#d0d0d0", "#c0c0c0"],
            height=140,
        )
        self.banner_frame.pack(fill="x", padx=0, pady=0)
        self.banner_frame.pack_propagate(False)
        
        # Título principal con diseño moderno
        title_frame = ctk.CTkFrame(self.banner_frame, fg_color="transparent")
        title_frame.pack(expand=True)
        
        main_title = ctk.CTkLabel(
            title_frame,
            text="PROGRAMADOR DE EVENTOS",
            font=("blue", 36, "bold"),
            text_color=["#000000", "#000000"]
        )
        main_title.pack(pady=5)
        
        subtitle = ctk.CTkLabel(
            title_frame,
            text="Sistema Profesional de Gestión",
            font=("Helvetica", 16),
            text_color=["#606060", "#606060"]
        )
        subtitle.pack()
        
        # Frame para el contenido (login/registro)
        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        self.content_frame.pack(pady=30, padx=20, fill="both", expand=True)
    
    def clear_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_login(self):
        self.clear_frame()
        
        # Frame para el formulario con efecto de tarjeta
        form_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=["#ffffff", "#f0f0f0"],
            corner_radius=15
        )
        form_frame.pack(pady=20, padx=40, ipady=20, ipadx=20)
        
        # Título del formulario
        title = ctk.CTkLabel(
            form_frame,
            text="Iniciar Sesión",
            font=("Helvetica", 24, "bold"),
            text_color=["#000000", "#000000"]
        )
        title.pack(pady=20)
        
        # Subtítulo
        subtitle = ctk.CTkLabel(
            form_frame,
            text="Accede a tu cuenta de organizador",
            font=("Helvetica", 14),
            text_color=["#606060", "#606060"]
        )
        subtitle.pack(pady=(0,20))
        
        # Campos de entrada estilizados
        self.login_username = ctk.CTkEntry(
            form_frame,
            placeholder_text="Ingrese su usuario o Email",
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.login_username.pack(pady=10)
        
        self.login_password = ctk.CTkEntry(
            form_frame,
            placeholder_text="Ingrese su Contraseña",
            show="•",
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.login_password.pack(pady=10)
        
        # Botón de recordar contraseña
        remember_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        remember_frame.pack(pady=(10,20))
        
        remember_checkbox = ctk.CTkCheckBox(
            remember_frame,
            text="Recordar mis datos",
            font=("Helvetica", 12),
            checkbox_width=20,
            checkbox_height=20,
            text_color=["#000000", "#000000"]
        )
        remember_checkbox.pack(side="left", padx=10)
        
        forgot_button = ctk.CTkButton(
            remember_frame,
            text="¿Olvidaste tu contraseña?",
            font=("Helvetica", 12),
            fg_color="transparent",
            hover_color=["#d0d0d0", "#c0c0c0"],
            text_color=["#000000", "#000000"]
        )
        forgot_button.pack(side="right", padx=10)
        
        # Botón de inicio de sesión
        login_button = ctk.CTkButton(
            form_frame,
            text="Log in",
            command= self.validate_login,
            width=350,
            height=45,
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            fg_color=["#007acc", "#005f99"],
            hover_color=["#005f99", "#004466"]
        )
        login_button.pack(pady=20)
        
        # Separador
        separator_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        separator_frame.pack(pady=10, fill="x")
        
        separator_line1 = ctk.CTkFrame(
            separator_frame,
            height=1,
            fg_color=["#d0d0d0", "#c0c0c0"]
        )
        separator_line1.pack(side="left", expand=True, padx=5, fill="x")
        
        separator_text = ctk.CTkLabel(
            separator_frame,
            text="O",
            font=("Helvetica", 12),
            text_color=["#606060", "#606060"]
        )
        separator_text.pack(side="left", padx=10)
        
        separator_line2 = ctk.CTkFrame(
            separator_frame,
            height=1,
            fg_color=["#d0d0d0", "#c0c0c0"]
        )
        separator_line2.pack(side="left", expand=True, padx=5, fill="x")
        
        # Botón de registro
        register_button = ctk.CTkButton(
            form_frame,
            text="Crear Nueva Cuenta",
            command=self.show_register,
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8,
            fg_color="transparent",
            border_width=1,
            border_color=["#007acc", "#005f99"],
            hover_color=["#d0d0d0", "#c0c0c0"],
            text_color=["#007acc", "#005f99"]
        )
        register_button.pack(pady=10)
    
    def show_register(self):
        self.clear_frame()
        
        # Frame para el formulario
        form_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=["#ffffff", "#f0f0f0"],
            corner_radius=15
        )
        form_frame.pack(pady=20, padx=40, ipady=20, ipadx=20)
        
        # Título
        title = ctk.CTkLabel(
            form_frame,
            text="Crear Cuenta",
            font=("Helvetica", 24, "bold"),
            text_color=["#000000", "#000000"]
        )
        title.pack(pady=20)
        
        # Subtítulo
        subtitle = ctk.CTkLabel(
            form_frame,
            text="Regístrate como organizador de eventos",
            font=("Helvetica", 14),
            text_color=["#606060", "#606060"]
        )
        subtitle.pack(pady=(0,20))
        
        # Campos de registro
        self.reg_username = ctk.CTkEntry(
            form_frame,
            placeholder_text="Nombre de usuario",
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.reg_username.pack(pady=10)
        
        self.reg_email = ctk.CTkEntry(
            form_frame,
            placeholder_text="Correo electrónico",
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.reg_email.pack(pady=10)
        
        self.reg_password = ctk.CTkEntry(
            form_frame,
            placeholder_text="Contraseña",
            show="•",
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.reg_password.pack(pady=10)
        
        self.reg_confirm_password = ctk.CTkEntry(
            form_frame,
            placeholder_text="Confirmar contraseña",
            show="•",
            width=350,
            height=45,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.reg_confirm_password.pack(pady=10)
        
        # Términos y condiciones
        terms_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        terms_frame.pack(pady=20)
        
        terms_checkbox = ctk.CTkCheckBox(
            terms_frame,
            text="Acepto los términos y condiciones",
            font=("Helvetica", 12),
            checkbox_width=20,
            checkbox_height=20,
            text_color=["#000000", "#000000"]
        )
        terms_checkbox.pack()
        
        # Botón de registro
        register_button = ctk.CTkButton(
            form_frame,
            text="Crear Cuenta",
            command=self.validate_signin,
            width=350,
            height=45,
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            fg_color=["#007acc", "#005f99"],
            hover_color=["#005f99", "#004466"]
        )
        register_button.pack(pady=20)
        
        # Enlace para volver al login
        login_link = ctk.CTkButton(
            form_frame,
            text="¿Ya tienes cuenta? Inicia sesión",
            command=self.show_login,
            font=("Helvetica", 12),
            fg_color="transparent",
            hover_color=["#d0d0d0", "#c0c0c0"],
            text_color=["#007acc", "#005f99"]
        )
        login_link.pack(pady=10)
    
    def validate_login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        
        if username == "" or password == "":
            messagebox.showinfo("Error", "Debes completar todos los campos")

        else:
            result = Database().validate_login(username, password)
            if result:
                messagebox.showinfo("Info", "Inicio de sesión correcto")
                self.destroy()
                app = Main_UI()
                app.mainloop()
            else:
                messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
           
    def validate_signin(self):
        username = self.reg_username.get()
        email = self.reg_email.get()
        password = self.reg_password.get()
        confirm_password = self.reg_confirm_password.get()

        user_names = Database().get_users_names(username)

        if username == "" or email == "" or password == "" or confirm_password == "":
            messagebox.showinfo("Error", "Debes completar todos los campos")
        elif password != confirm_password:
            messagebox.showinfo("Error", "Las contraseñas no coinciden")
        
        elif user_names:
            messagebox.showinfo("Error", "El nombre de usuario ya está en uso, elija otro")

        else:
            result = Database().add_user(username, email, password)
            if result  :
                messagebox.showinfo("Info", "Usuario registrado correctamente")
            else:
                messagebox.showinfo("Error", "Error al registrar usuario")
        
       

