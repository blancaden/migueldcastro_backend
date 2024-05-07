from flask import Blueprint, request
from src.services.WorkshopServices import WorkshopServices
from src.models.workshopModel import Workshop

main = Blueprint('workshop_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_workshop():
    
    get_workshop=WorkshopServices.get_workshop()
    print(get_workshop)

    print('Esto se imprime en consola, GET')
    return 'Get exitoso'


@main.route('/create',methods=['POST'])
def post_workshop():

    ID_Talleres = ""
    ID_Usuario = request.json['ID_Usuario']
    Titulo = request.json['Titulo']
    Fecha = request.json['Fecha']
    Lugar = request.json['Lugar']
    Horario = request.json['Horario']
    Imagen = request.json['Imagen']

    workshop1 = Workshop(ID_Talleres,ID_Usuario,Titulo,Fecha,Lugar,Horario,Imagen)

    post_workshop=WorkshopServices.post_workshop(workshop1)
    print(post_workshop)

    print('Esto se imprime en consola, POST')
    return 'Create exitoso'


@main.route('/update',methods=['PUT'])
def update_workshop():

    ID_Talleres = request.json['ID_Talleres']
    ID_Usuario = request.json['ID_Usuario']
    Titulo = request.json['Titulo']
    Fecha = request.json['Fecha']
    Lugar = request.json['Lugar']
    Horario = request.json['Horario']
    Imagen = request.json['Imagen']

    workshop1 = Workshop(ID_Talleres,ID_Usuario,Titulo,Fecha,Lugar,Horario,Imagen)

    update_workshop=WorkshopServices.update_workshop(workshop1)
    print(update_workshop)

    print('Esto se imprime en consola, PUT')
    return 'Update exitoso'


@main.route('/remove',methods=['DELETE'])
def delete_workshop():

    ID_Talleres = request.json['ID_Talleres']

    delete_workshop=WorkshopServices.delete_workshop(ID_Talleres)
    print(delete_workshop)

    print('Esto se imprime en consola, DELETE')
    return 'Delete exitoso'