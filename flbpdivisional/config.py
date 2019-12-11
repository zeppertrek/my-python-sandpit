#config.py

class BaseConfig:
    SECRET_KEY = 'MUTTLIPUTTLI'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    ##### Flask-Mail configurations #####
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =  'infooveriq@gmail.com'
    MAIL_PASSWORD =  'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
 
 
class DevelopmentConfig(BaseConfig):
    #DEBUG = True
    MAIL_USE_TLS = False 
    SECRET_KEY = 'MUTTLIPUTTLI'
    
 
class TestingConfig(BaseConfig):
    #DEBUG = True
    MAIL_USE_TLS = False
 
class ProductionConfig(BaseConfig):
    #DEBUG = False
    MAIL_USE_TLS = False
