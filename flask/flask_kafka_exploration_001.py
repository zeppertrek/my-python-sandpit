#flask_kafka_exploration_001.py 

# set FLASK_APP=flask_kafka_exploration_001.py
# set FLASK_DEBUG=1
# python -m flask run
# This will run a development server that is NOT meant to be used for production purposes 
# 
# Using httpie as a tool to test the request 
# http POST http://127.0.0.1:5000/kafprod kafkey=1000 kafmsg=1002
# http POST http://127.0.0.1:5000/prodkaf kafmsg="This is my FIRST test msg" 
# http GET http://127.0.0.1:5000/kafcons 
# 
# 
# List of recommended Python Kafka clients 
# 
# >> https://pypi.org/project/kafka-python/  [USED IN THIS PROGRAM]
# >> https://github.com/Parsely/pykafka
# >> Confluent's client  https://github.com/confluentinc/confluent-kafka-python (May not work on Windows)


# 
# This is a very basic Kafka example involving a producer and a consumer  
# Any sensible python program WILL NOT have a producer and consumer in the same module !
#

from flask import Flask, request, redirect, url_for, jsonify
#
from time import sleep
from json import dumps
from json import loads 
# 
from kafka import KafkaProducer
from kafka import KafkaConsumer

#producer = KafkaProducer(bootstrap_servers='localhost:29092')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
#
#consumer = KafkaConsumer( 'pytop', bootstrap_servers=['localhost:29092'], auto_offset_reset='earliest', enable_auto_commit=True )

# group_id - ? 
# 
consumer = KafkaConsumer(
    'covid19',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id="covid19-group-2",
     value_deserializer=lambda x: loads(x.decode('utf-8')))


#producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')



app = Flask(__name__)


@app.route('/kafprod', methods=['POST'])
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
	

@app.route('/prodkaf', methods=['POST'])
def handle_prodkaf():
    if request.method == 'POST':
        if request.is_json:
            #
            # Include code ober 
            # 
            data = request.get_json()
            # producer.send('pytop', data['kafmsg'])
            #kafkamessage = {'mmssgg' : data['kafmsg']}
            for i in range(5000):
                kafkamessage = {'mmssgg' : data['kafmsg'] + "--" + str(i) + ">>" } 
                producer.send('covid19', value=kafkamessage)
            # 
            return {"message": f"Message sent successfully to the topic pytop at localhost - 127.0.0.1" + data['kafmsg'] }
        else:
            return {"error": "The request payload is not in JSON format"}

@app.route('/kafcons', methods=['GET'])
def handle_kafcons():
    lastmsg = "X" 
    for message in consumer:
        lastmsg = message.value
    return {"last message consumed : ", lastmsg }



@app.route('/kc2', methods=['GET'])
def handle_kc2():
    while True:
        raw_messages = consumer.poll(timeout_ms=1000, max_records=5000)
        for topic_partition, messages in raw_messages.items():
            application_message = json.loads(message.value.decode())	