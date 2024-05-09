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
                    
                    return {'Nombre': result[0]}
                     
                else:
                
                  
                    return None
        except Exception as ex:
            
            print(ex)
    @classmethod
    def generate_token(cls, Name):
        payload = {'Name': Name}
        secret_key = Config.SECRET_KEY  # Utiliza la clave secreta de la configuración
        algorithm = 'HS256'  # Algoritmo de encriptación
        
        # Generar el token utilizando la librería JWT
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        
        return token
