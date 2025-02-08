import pyodbc

server = 'localhost'
database = 'Eventos'
usuario = 'Johan'
contraseña = '1522'

class Database:
    def get_connection(self):
        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + usuario + ';PWD=' + contraseña)

            return conexion
        except Exception as e:
            print("Error de conexión: ", e)
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
    
   

   
