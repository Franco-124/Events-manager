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

   

   
