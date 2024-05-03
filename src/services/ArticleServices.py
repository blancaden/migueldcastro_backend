from src.database.db_mysql import get_connection;
from src.models.articleModel import Article

class ArticleServices():

    @classmethod
    def get_articles(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection.cursor() as data_castro:
                data_castro.execute('SELECT * FROM articulo')
                result= data_castro.fetchall()
                print(result)
            
            connection.close()
            return 'Articulos mostrados'

        except Exception as ex:
            print(ex)

    @classmethod
    def create_articles(cls, article: Article):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as data_castro:
                ID_Articulo = article.ID_Articulo
                ID_Usuario = article.ID_Usuario
                Titulo = article.Titulo
                Contenido = article.Contenido
                Fecha = article.Fecha
                Imagen = article.Imagen

                
                data_castro.execute("INSERT INTO `articulo` (`ID_Articulo`, `ID_Usuario`, `Titulo`, `Contenido`, `Fecha`, `Imagen`) VALUES (%s, %s, %s, %s, %s, %s);",
                                     (ID_Articulo, ID_Usuario, Titulo, Contenido, Fecha, Imagen))
                connection.commit()
            
            connection.close()
            return 'Articulo ingresado'

        except Exception as ex:
            print(ex)


    @classmethod
    def update_articles(cls, article: Article):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as data_castro:
                ID_Articulo = article.ID_Articulo
                ID_Usuario = article.ID_Usuario
                Titulo = article.Titulo
                Contenido = article.Contenido
                Fecha = article.Fecha
                Imagen = article.Imagen


                data_castro.execute("UPDATE articulo SET ID_Usuario = %s, Titulo = %s, Contenido = %s, Fecha = %s, Imagen = %s WHERE ID_Articulo = %s",
                                     (ID_Usuario, Titulo, Contenido, Fecha, Imagen, ID_Articulo))
                connection.commit()

            connection.close()
            return 'Articulo actualizado'

        except Exception as ex:
            print(ex)



    @classmethod
    def delete_articles(cls, ID_Articulo: int):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as data_castro:

                data_castro.execute("DELETE FROM articulo WHERE ID_Articulo = %s", (ID_Articulo))
                connection.commit()

            connection.close()
            return 'Articulo eliminado'

        except Exception as ex:
            print(ex)