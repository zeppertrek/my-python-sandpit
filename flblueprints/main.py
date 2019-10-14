# main.py
# set FLASK_APP=main.py
# set FLASK_DEBUG=1
# python -m flask run

# Read more to understand why this import works !. create_app is inside __init__.py 
from flblueprints import create_app

# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/flask.cfg

# Note - create_app function is in the __init__.py file under flblueprints folder 
app = create_app('flask.cfg')
