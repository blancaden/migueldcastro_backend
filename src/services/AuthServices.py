from ..database.db_mysql import get_connection
from flask import jsonify
import jwt
from config import Config

class AuthServices():
    @classmethod
    def authenticate(cls, Nombre, Contraseña):
        try: 
            connection = get_connection()
            with connection.cursor() as cursor:
             
                cursor.execute("SELECT Nombre, Contraseña FROM usuario WHERE Nombre = %s AND Contraseña = %s", (Nombre, Contraseña))
                print(Nombre)
                print(Contraseña)
                
                result = cursor.fetchone()
                print (result)
                if result:
                    # Si se encuentra un usuario con las credenciales proporcionadas, retornar los datos del usuario
                    # return {'username': result['username'], 'role': result['role']}
                    print("ssssssaaaaaa")
                    return {'Nombre': result[0]}
                     
                else:
                    # Si no se encuentra un usuario con esas credenciales, retornar None
                  
                    return None
        except Exception as ex:
            # Manejar cualquier excepción que pueda ocurrir durante la autenticación
            print(ex)
    @classmethod
    def generate_token(cls, Name):
        payload = {'Name': Name}
        secret_key = Config.SECRET_KEY  # Utiliza la clave secreta de la configuración
        algorithm = 'HS256'  # Algoritmo de encriptación
        
        # Generar el token utilizando la librería JWT
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        
        return token
