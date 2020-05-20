# [SANJIV NAGRAJ ] 
# __init__.py for flblueprints\flblueprints
# Initialization code for this package  
from flask import Flask
from flask_login import LoginManager
import os


#
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt


#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
# Need to understand in a FLASK APP what should be defined globally 
# 
pdbx = SQLAlchemy()
#bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "users.login"


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
    #
    # Logging
    import logging 	
    from logging.config import dictConfig
    #from flblueprints.logging_config import flloggingconfig
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

    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_pyfile(config_filename)
    # Read up on the use of the instance folder that one can use in Flask 
    # app.config.from_pyfile ("D:/workspaces/my-python-sandpit/flblueprints/instance/flask.cfg")
	# The instance folder is designed to not be under version control and be deployment specific
    # There are different ways of obtaining the run time configuration 

    #1. From a file  
    #app.config.from_pyfile (config_filename)

    # Both statements below did not work 
    #from flblueprints.config import BaseConfig, DevelopmentConfig, TestingConfig, ProductionConfig
    #from flblueprints import config
    # works when config.py is located in the root folder 
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
	
    #app.config.from_object(app_config)
	
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
    pdbx.init_app(app)
    #bcrypt.init_app(app)
    login.init_app(app)

    # Flask-Login configuration
    from flblueprints.models import SteroidUser
    #from . import db
    # need to fully understand the logic for correctly referencing a package/module/function while importing 
    from flblueprints.users.db.user_db import user_db_list	
	
    #def load_user(user_id):
    #    return User.query.filter(User.id == int(user_id)).first()
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
    from flblueprints.cookiecutter import cookiecutter_blueprint
    from flblueprints.recipes import recipes_blueprint
    from flblueprints.users import users_blueprint

    app.register_blueprint(cookiecutter_blueprint)
    app.register_blueprint(recipes_blueprint)
    app.register_blueprint(users_blueprint)
