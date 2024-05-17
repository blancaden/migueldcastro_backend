from flask import Blueprint, request, jsonify
from src.services.FormServices import FormServices
from src.models.formModel import Form

main = Blueprint('form_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_form():
    
    get_form=FormServices.get_form()
    print(get_form)

    print('Esto se imprime en consola, GET')
    return jsonify(get_form)


@main.route('/create',methods=['POST'])
def post_form():

    ID_Contacto = ""
    Nombre = request.json['Nombre']
    Email = request.json['Email']
    Mensaje = request.json['Mensaje']
    Asunto= request.json['Asunto']

    form1 = Form(ID_Contacto,Nombre,Email,Mensaje,Asunto)

    post_form=FormServices.post_form(form1)
    print(post_form)

    print('Esto se imprime en consola, POST')
    return 'Create exitoso'

@main.route('/remove',methods=['DELETE'])
def delete_form():

    ID_Contacto = request.json['ID_Contacto']

    delete_form=FormServices.delete_form(ID_Contacto)
    print(delete_form)

    print('Esto se imprime en consola, DELETE')
    return 'Delete exitoso'