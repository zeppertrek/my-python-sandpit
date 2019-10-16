# [SANJIV NAGRAJ]
# flblueprints/users/__init__.py
# this is the  initialization file for flblueprints/users 
# 
"""
The users Blueprint handles the user management for this application.
Specifically, this Blueprint allows for new users to register and for
users to log in and to log out of the application.
"""
from flask import Blueprint
users_blueprint = Blueprint('users', __name__, template_folder='templates')

# This is at the end . There should be a reason for this 
from . import routes
