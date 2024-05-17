from flask import Flask
from flask_cors import CORS

from .routes.UserRoutes import user_routes


# Routes
from .routes import ArticleRoutes
from .routes import WorkshopRoutes
from .routes import FormRoutes

def init_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Habilitar CORS, está bien pero no es muy recomendado entonces abajo 
    #aclaramos otra manera de agregar los distintos orígenes que se puede ir aceptando
                     # CORS(app)
    
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://otro-origen.com"]}})

    # Registrar blueprints
    app.register_blueprint(ArticleRoutes.main, url_prefix='/articulos')
    app.register_blueprint(user_routes)
    app.register_blueprint(WorkshopRoutes.main, url_prefix='/talleres')
    app.register_blueprint(FormRoutes.main, url_prefix='/contacto')

    return app
