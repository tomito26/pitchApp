import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:tom@localhost/pitchapp'

class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production':prodConfig
}