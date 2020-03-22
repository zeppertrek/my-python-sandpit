#flask_kafka_exploration_001.py 

# set FLASK_APP=flask_kafka_exploration_001.py
# set FLASK_DEBUG=1
# python -m flask run
# This will run a development server that is NOT meant to be used for production purposes 
# 
# Using httpie as a tool to test the request 
# http POST http://127.0.0.1:5000/kafprod kafkey=1000 kafmsg=1002
# http GET http://127.0.0.1:5000/kafcons  redkey 
# 
# 
# List of recommended Python Kafka clients 
# 
# >> https://pypi.org/project/kafka-python/  [USED IN THIS PROGRAM]
# >> https://github.com/Parsely/pykafka
# >> Confluent's client  https://github.com/confluentinc/confluent-kafka-python (May not work on Windows)


# 
# This is a very basic Kafka example involving a producer and a consumer  
#

from flask import Flask, request, redirect, url_for, jsonify
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
#producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')



app = Flask(__name__)


@app.route('/kafprod', methods=['POST', 'GET'])
def handle_kafprod():
    if request.method == 'POST':
        if request.is_json:
            #
            # Include code ober 
            # 
            data = request.get_json()
            producer.send('pytop', b'This is a test msg')
            return {"message": f"Message sent successfully to the topic pytop at localhost - 127.0.0.1"}
        else:
            return {"error": "The request payload is not in JSON format"}
    elif request.method == 'GET':
        return {"Key": data['redkey'], "Value": redis_client.get(data['redkey'])}
        #return "test return value"
		
		

@app.route('/kafcons', methods=['POST', 'GET'])
def handle_kafcons():
    if request.method == 'POST':
        if request.is_json:
            #
            # Include code ober 
            # 
            return {"message": f"Key {data['redkey']} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    elif request.method == 'GET':
        return {"Key": data['redkey'], "Value": redis_client.get(data['redkey'])}
        #return "test return value"