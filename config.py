import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:tom@localhost/pitchsite'

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # simple mde configurations
    SIMPLEDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False


class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:tom@localhost/pitchapp_test'
    pass


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:tom@localhost/pitchapp'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}