#flask_rest_api_example_001.py

from flask import Flask
# Instead of using this: from flask.ext.restful import  Api
# Use this:
from flask.ext.restful_swagger_2 import Api

app = Flask(__name__)

# Use the swagger Api class as you would use the flask restful class.
# It supports several (optional) parameters, these are the defaults:
api = Api(app, api_version='0.0', api_spec_url='/api/swagger')