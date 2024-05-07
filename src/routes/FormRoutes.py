from flask import Blueprint, request
from src.services.FormServices import FormServices
from src.models.formModel import Form

main = Blueprint('form_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_form():
    
    get_form=FormServices.get_form()
    print(get_form)

    print('Esto se imprime en consola, GET')
    return 'Get exitoso'


@main.route('/create',methods=['POST'])
def post_form():

    ID_Contacto = ""
    Nombre = request.json['Nombre']
    Email = request.json['Email']
    Mensaje = request.json['Mensaje']
    Fecha = request.json['Fecha']

    form1 = Form(ID_Contacto,Nombre,Email,Mensaje,Fecha)

    post_form=FormServices.post_form(form1)
    print(post_form)

    print('Esto se imprime en consola, POST')
    return 'Create exitoso'