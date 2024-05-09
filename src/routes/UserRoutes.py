from flask import Blueprint, request, jsonify
from src.services.AuthServices import AuthServices

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/api/login', methods=['POST'])
def login():
    name = request.json.get('Nombre')
    print (name)
    password = request.json.get('Contraseña') 
    print (password)
    user_data = AuthServices.authenticate(name, password)
    print(user_data)
    
    if user_data:
        token = AuthServices.generate_token(name)
        
        response = {
            'token': token
        }
        
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Datos  no válidos'}), 401
