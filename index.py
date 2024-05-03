from flask import Flask
from flask_cors import CORS
from src import init_app
from config import config

configuration = config['development']

app = init_app(configuration)

# Aplica la configuración CORS después de inicializar app
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)