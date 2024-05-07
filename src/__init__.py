from flask import Flask
from flask_cors import CORS

from .routes.UserRoutes import user_routes


# Routes
from .routes import ArticleRoutes
# from .routes import WorkshopRoutes
# from .routes import FormRoutes

def init_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Habilitar CORS
    CORS(app)

    # Registrar blueprints
    app.register_blueprint(ArticleRoutes.main, url_prefix='/articulos')
    app.register_blueprint(user_routes)
    # app.register_blueprint(WorkshopRoutes.main, url_prefix='/talleres')
    # app.register_blueprint(FormRoutes.main, url_prefix='/contacto')

    return app
