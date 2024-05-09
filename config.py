import secrets

class Config:
    DEBUG = False
    SECRET_KEY = secrets.token_hex(32)  # Genera una clave secreta aleatoria
    JWT_SECRET_KEY = 'tu_clave_secreta_para_jwt'  # Clave secreta para firmar tokens JWT

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': Config
}
















#### como lo traje originalmente de configuración de stefi#####
# class DevelopmentConfig():
#     DEBUG = True

# config={
#     'development': DevelopmentConfig
# }