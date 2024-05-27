import pytest

from src.services.FormServices import FormServices
from src.models.formModel import Form


@pytest.fixture(scope='session')
def users():
    return FormServices.get_form()

@pytest.fixture(scope='session')
def new_user_data():
    # Define los datos para simular la entrada de un nuevo usuario
    return {
        "ID_Contacto": 13,
        "Nombre": "Blanca",
        "Email": "nuevo_usuario@example.com",
        "Mensaje": "Este es un mensaje de prueba para el nuevo usuario",
        "Asunto": "Nuevo Usuario"
    }

def test_get_user_not_none(users):
    assert users != None

def test_get_user_isinstance_of_list(users):
    assert isinstance(users,list)

def test_create_new_user(new_user_data):

    form = Form(ID_Contacto=new_user_data['ID_Contacto'], 
                Nombre=new_user_data['Nombre'], 
                Email=new_user_data['Email'], 
                Mensaje=new_user_data['Mensaje'], 
                Asunto=new_user_data['Asunto'])

   
    result = FormServices.post_form(form)

    
    assert result == 'Formulario ingresado'


def test_delete_user(users):
    # ID_Contacto del usuario a eliminar
    id_to_delete = 12
    
    # Verificar que el usuario con ID_Contacto=id_to_delete existe antes de eliminar
    assert any(user['ID_Contacto'] == id_to_delete for user in users)

    # Eliminar el usuario
    result = FormServices.delete_form(id_to_delete)
    
    assert result == 'Usuario eliminado'

    # Verificar que el usuario ha sido eliminado
    users_after_deletion = FormServices.get_form()
    assert not any(user['ID_Contacto'] == id_to_delete for user in users_after_deletion)


 
    