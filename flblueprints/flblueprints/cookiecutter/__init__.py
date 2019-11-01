#[SANJIV NAGRAJ]
#flblueprints/cookiecutter/__init__.py
# Initialization code for this package 

"""
The cookiecutter Blueprint handles the creation, modification, deletion,and viewing of cookies for this application.
"""
from flask import Blueprint
cookiecutter_blueprint = Blueprint('cookiecutter', __name__, template_folder='templates')

from . import routes
