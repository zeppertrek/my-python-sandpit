#config.py

class BaseConfig:
    SECRET_KEY = 'C@TS DOGZ D0NT MIQX 2 WELL'

 
class DevelopmentConfig(BaseConfig):
    #DEBUG = True
    ENV_FLAG = "DEV"    
 
class TestingConfig(BaseConfig):
    #DEBUG = True
    ENV_FLAG = "TEST"    
 
class ProductionConfig(BaseConfig):
    #DEBUG = False
    ENV_FLAG = "PROD"    
