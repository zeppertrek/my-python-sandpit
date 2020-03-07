#flask_redis_exploration_001.py 

# set FLASK_APP=flask_redis_exploration_001.py
# set FLASK_DEBUG=1
# python -m flask run
# This will run a development server that is NOT meant to be used for production purposes 
# 
# Using httpie as a tool to test the request 
# http POST http://127.0.0.1:5000/redreq redkey=1000 redval=1002
# http GET http://127.0.0.1:5000/redreq  redkey 
# 
# 
# This is a very basic REDIS example 
# REDIS_URL = "redis://:password@localhost:6379/0"  (MUST BE SET)
# The underlying package is redis-py. 
# The redis client created below from FlaskRedis acts just like a regular Redis instance from the redis-py library
#

from flask import Flask, request, redirect, url_for, jsonify
from flask_redis import FlaskRedis

app = Flask(__name__)
# app.config['REDIS_HOST'] = 'localhost'
# app.config['REDIS_PORT'] = 6379
# app.config['REDIS_DB'] = 0
#
app.config ['REDIS_URL'] = "redis://localhost:6379/0"
redis_client = FlaskRedis(app)



@app.route('/redreq', methods=['POST', 'GET'])
def handle_redreq():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            redis_client.getset(data['redkey'], data['redval'])
            return {"message": f"Key {data['redkey']} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        data = request.get_json()
        return {"Key": data['redkey'], "Value": redis_client.get(data['redkey'])}
        #return "test return value"