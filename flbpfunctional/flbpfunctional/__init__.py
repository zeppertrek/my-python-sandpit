# __init__py for flbpfunctional 
# 

# Initialization code for this package  
from flask import Flask
from flask_login import LoginManager
import os


# Flask-Login configuration
# Giving this global scope 
from flbpfunctional.models import SteroidUser
#from . import db
# need to fully understand the logic for correctly referencing a package/module/function while importing 
from flbpfunctional.db.user_db import user_db_list	

#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.

login = LoginManager()
login.login_view = "users.login"


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
    #
    # Logging -- Approach needs improvement.  Can this go into the global scope 
    import logging 	
    from logging.config import dictConfig
    dictConfig({
        'version': 1,
        'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
})

	
    #logging.config.dictConfig(dictConfig)
    # Explore the various options when creating a flask app 
    app = Flask(__name__, instance_relative_config=True)
    # 	
    environment_type = os.environ.get('FLASK_ENV')
    if environment_type == 'development':
        #Uses objects.   
        app.config.from_object("config.DevelopmentConfig")
    elif environment_type == 'development':
        app_config = TestingConfig()
    elif environment_type == 'production':
        app_config = ProductionConfig()
    else:
        app_config = DevelopmentConfig()        	
    initialize_extensions(app)
    register_blueprints(app)
    app.logger.info ("Blueprints initialized and registered")
    return app


##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    login.init_app(app)

    # Flask-Login configuration
    #from flbpfunctional.models import SteroidUser
    #from . import db
    # need to fully understand the logic for correctly referencing a package/module/function while importing 
    #from flbpfunctional.db.user_db import user_db_list	
	
    @login.user_loader
    def user_loader(email):
        if email not in user_db_list.keys():
            return None 

        user = SteroidUser()
        user.id = email
        user.email = email 
        return user

def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from flbpfunctional.views.admin import users_blueprint
    app.register_blueprint(users_blueprint)
