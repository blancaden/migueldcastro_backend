from flask import Blueprint, request
from src.services.ArticleServices import ArticleServices
from src.models.articleModel import Article

main = Blueprint('articles_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_articles():
    
    get_articles=ArticleServices.get_articles()
    print(get_articles)

    print('Esto se imprime en consola, GET')
    return 'Get exitoso'


@main.route('/create',methods=['POST'])
def post_articles():

    ID_Articulo = ""
    ID_Usuario = request.json['ID_Usuario']
    Titulo = request.json['Titulo']
    Contenido = request.json['Contenido']
    Fecha = request.json['Fecha']
    Imagen = request.json['Imagen']

    article1 = Article(ID_Articulo,ID_Usuario,Titulo,Contenido,Fecha,Imagen)

    post_articles=ArticleServices.post_articles(article1)
    print(post_articles)

    print('Esto se imprime en consola, POST')
    return 'Create exitoso'


@main.route('/update',methods=['PUT'])
def update_articles():

    ID_Articulo = request.json['ID_Articulo']
    ID_Usuario = request.json['ID_Usuario']
    Titulo = request.json['Titulo']
    Contenido = request.json['Contenido']
    Fecha = request.json['Fecha']
    Imagen = request.json['Imagen']

    article1 = Article(ID_Articulo,ID_Usuario,Titulo,Contenido,Fecha, Imagen)

    update_articles=ArticleServices.update_articles(article1)
    print(update_articles)

    print('Esto se imprime en consola, PUT')
    return 'Update exitoso'


@main.route('/remove',methods=['DELETE'])
def delete_articles():

    ID_Articulo = request.json['ID_Articulo']

    delete_articles=ArticleServices.delete_articles(ID_Articulo)
    print(delete_articles)

    print('Esto se imprime en consola, DELETE')
    return 'Delete exitoso'