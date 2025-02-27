import pyodbc

from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
usuario = os.getenv('DB_USER')
contraseña = os.getenv('DB_PASSWORD')

class Database:
    def get_connection(self):
        try:
            conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={usuario};'
                f'PWD={contraseña}'
            )

            return conexion
        except pyodbc.InterfaceError as e:
            print("Error de conexión: No se pudo conectar a la base de datos. Verifica el servidor y las credenciales.")
            print("Detalles del error:", e)
            return None
        
        except pyodbc.DatabaseError as e:
            print("Error de conexión: Hubo un problema con la base de datos.")
            print("Detalles del error:", e)
            return None

        except Exception as e:
            print("Error de conexión: Ocurrió un error inesperado.")
            print("Detalles del error:", e)
            return None
    

    def add_user (self, user_name:str, email: str, password:str):
        try:
            conexion = self.get_connection()
            cursor = conexion.cursor()
            # Llamar al procedimiento almacenado
            cursor.execute("EXEC agregar_usuario @nombre = ?, @email = ?, @contraseña = ?", 
                        (user_name, email, password))
            conexion.commit()
            conexion.close()

            return True
        
        except Exception as e:
            print("Error al agregar usuario: ", e)
            return False
    
    def get_users_names(self, user_name:str):
        try:
            conexion = self.get_connection()
            cursor = conexion.cursor()
            cursor.execute("EXEC obtener_usuarios @nombre = ?", (user_name))
            users = cursor.fetchall()
            conexion.close()

            return users
        
        except Exception as e:
            print("Error al obtener usuarios: ", e)
            return None


    def validate_login(self, user_name:str, password:str):
        try:
            conexion = self.get_connection()
            cursor = conexion.cursor()
            cursor.execute("EXEC buscar_usuario @nombre = ?, @contraseña = ?", 
                           (user_name, password))
            user = cursor.fetchall()
            conexion.close()

            if user:
                return True
            else:
                return None
        
        except Exception as e:
            print("Error al obtener usuarios: ", e)
            return None
    
   

   
