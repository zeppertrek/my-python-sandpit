# [SANJIV NAGRAJ]
#/flblueprints/alchemy/routes.py

#################
#### imports ####
#################

from flask import render_template
from flask_login import login_required

#from . import users_blueprint
#from .forms import RegisterForm, LoginForm
from flblueprints.pdbmodels import Mp


################
#### routes ####
################

@alchemy.route('/mpinsert')
def mpinsert():
    return render_template('alchemy/dbinsert.html')

