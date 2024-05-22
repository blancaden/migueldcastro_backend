from src.database.db_mysql import get_connection;
from src.models.formModel import Form;

class FormServices():

    @classmethod
    def get_form(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection.cursor() as data_castro:
                data_castro.execute('SELECT * FROM contacto')
                result= data_castro.fetchall()
                
            user_objects = []
            for user in result:
                usuario = {
                    'ID_Contacto': user[0],
                    'Nombre': user[1],
                    'Email': user[2],
                    'Mensaje': user[3],
                    'Asunto': user[4]
                }
                user_objects.append(usuario)
                
                print(result)
            
            connection.close()
            return user_objects

        except Exception as ex:
            print(ex)

    @classmethod
    def post_form(cls, form: Form):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as data_castro:
                ID_Contacto = form.ID_Contacto
                Nombre = form.Nombre
                Email = form.Email
                Mensaje = form.Mensaje
                Asunto = form.Asunto

                
                data_castro.execute("INSERT INTO `contacto` (`ID_Contacto`, `Nombre`, `Email`, `Mensaje`, `Asunto`) VALUES (%s, %s, %s, %s, %s);",
                                     (ID_Contacto, Nombre, Email, Mensaje, Asunto))
                connection.commit()
            
            connection.close()
            return 'Formulario ingresado'

        except Exception as ex:
            print(ex)

    @classmethod
    def delete_form(cls, ID_Contacto: int):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as data_castro:
                data_castro.execute("DELETE FROM contacto WHERE ID_Contacto = %s", (ID_Contacto,))
                connection.commit()

            connection.close()
            return 'Usuario eliminado'

        except Exception as ex:
            print(ex)
            return 'Error al eliminar el usuario'