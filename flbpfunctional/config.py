#config.py

class BaseConfig:
    SECRET_KEY = 'MUTTLIPUTTLI'
    
	
class DevelopmentConfig(BaseConfig):
    #DEBUG = True
    RUNTIME_ENV="DEV"    
 
class TestingConfig(BaseConfig):
    #DEBUG = True
    RUNTIME_ENV="TEST"    
 
class ProductionConfig(BaseConfig):
    #DEBUG = False
    RUNTIME_ENV="PROD"    
