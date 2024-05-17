from src.database.db_mysql import get_connection;
from src.models.workshopModel import Workshop

class WorkshopServices():

    @classmethod
    def get_workshop(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection.cursor() as data_castro:
                data_castro.execute('SELECT * FROM talleres')
                result= data_castro.fetchall()

            workshop_objects = []
            for workshop in result:
                art = {
                    'ID_Talleres': workshop[0],
                    'ID_Usuario': workshop[1],
                    'Titulo': workshop[2],
                    'Fecha': workshop[3],
                    'Lugar': workshop[4],
                    'Horario': workshop[5],
                    'Imagen': workshop[6],
                    'Descripción': workshop[7]
                }
                workshop_objects.append(art)  
            
            connection.close()
            return workshop_objects

        except Exception as ex:
            print(ex)

    @classmethod
    def post_workshop(cls, workshop: Workshop):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as data_castro:
                ID_Talleres = workshop.ID_Talleres
                ID_Usuario = workshop.ID_Usuario
                Titulo = workshop.Titulo
                Fecha = workshop.Fecha
                Lugar = workshop.Lugar
                Horario = workshop.Horario
                Imagen = workshop.Imagen
                Descripción = workshop.Descripción

                
                data_castro.execute("INSERT INTO `talleres` (`ID_Talleres`, `ID_Usuario`, `Titulo`, `Fecha`, `Lugar`, `Horario`, `Imagen`, `Descripción`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                                     (ID_Talleres, ID_Usuario, Titulo, Fecha, Lugar, Horario, Imagen, Descripción))
                connection.commit()
            
            connection.close()
            return 'Taller ingresado'

        except Exception as ex:
            print(ex)


    @classmethod
    def update_workshop(cls, workshop: Workshop):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as data_castro:
                ID_Talleres = workshop.ID_Talleres
                ID_Usuario = workshop.ID_Usuario
                Titulo = workshop.Titulo
                Fecha = workshop.Fecha
                Lugar = workshop.Lugar
                Horario = workshop.Horario
                Imagen = workshop.Imagen
                Descripción = workshop.Descripción


                data_castro.execute("UPDATE talleres SET ID_Usuario = %s, Titulo = %s, Lugar = %s, Horario = %s, Fecha = %s, Imagen = %s, Descripción = %s WHERE ID_Talleres = %s",
                                     (ID_Usuario, Titulo, Lugar, Horario, Fecha, Imagen, Descripción, ID_Talleres))
                connection.commit()

            connection.close()
            return 'Taller actualizado'

        except Exception as ex:
            print(ex)



    @classmethod
    def delete_workshop(cls, ID_Talleres: int):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as data_castro:

                data_castro.execute("DELETE FROM talleres WHERE ID_Talleres = %s", (ID_Talleres))
                connection.commit()

            connection.close()
            return 'Taller eliminado'

        except Exception as ex:
            print(ex)