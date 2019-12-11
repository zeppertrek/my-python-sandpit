# main.py
# This is the main calling program for the flblueprints flask web application 
#
#  With blueprints, we can think of choices as functional versus divisional. follow best practices over here. 
#  This project uses the divisional approach 
# organize the pieces of the application based on which part of the app they contribute to
# 
# set FLASK_APP=main.py
# set FLASK_DEBUG=1
# python -m flask run
# 
# Using waitress - a WSGI server 
# waitress-serve  main:app 

# export/set FLASK_ENV=development
# Always set FLASK_ENV/FLASK_DEBUG at the OS level before launching the flask app NEVER in your program 
# Do not enable debug mode when deploying in production

# Read more to understand why this import works !. create_app is inside __init__.py 
# If the module/func is not found, then python looks into __init__.py for the package - that's why !
import os  
from flbldivisional import create_app

# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/flask.cfg

# Note - create_app function is in the __init__.py file under flblueprints folder 

app_dir = os.path.abspath(os.path.dirname(__file__))
print ( app_dir)
app_dir = app_dir + "/instance" 
print ( app_dir)
cfg_file = app_dir + "/flask.cfg"
print (cfg_file)
app = create_app(cfg_file)
