#[SANJIV NAGRAJ]
#flblueprints/cookiecutter/routes.py

#################
#### imports ####
#################

from flask import render_template

from . import cookiecutter_blueprint


################
#### routes ####
################

@cookiecutter_blueprint.route('/cookie')
def index():
    return render_template('cookiecutter/index.html')


