#fl_rest_api_app.py
#!/usr/bin/env python

# set FLASK_APP=fl_rest_api_app.py
# set FLASK_DEBUG=1
# python -m flask run


# NOTE: Run with PYTHONPATH=. python example/app.py

from flask import Flask
# A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
from flask_cors import CORS
# Extract swagger specs from your flask-restful project.
from flask_restful_swagger_2 import Api, swagger

from fl_rest_api_views import UserResource, UserItemResource, GroupResource

app = Flask(__name__)
CORS(app)
api = Api(app, api_version='0.1')


def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    return True


swagger.auth = auth

api.add_resource(UserResource, '/api/users')
api.add_resource(UserItemResource, '/api/users/<int:user_id>')
api.add_resource(GroupResource, '/api/groups/')


@app.route('/')
def index():
    return """<head>
    <meta http-equiv="refresh" content="0; url=http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json" />
    </head>"""


if __name__ == '__main__':
    app.run(debug=True)