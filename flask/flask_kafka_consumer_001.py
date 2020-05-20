#flask_kafka_consumer_001.py 

# set FLASK_APP=flask_kafka_consumer_001.py
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
from confluent_kafka import Consumer, KafkaError


app = Flask(__name__)

@app.route('/kafcons', methods=['GET'])
def handle_kafcons():
#

    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my-c19-group',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe(['covid19'])
    i = 0 ;
    print ("After subscribe and before While TRUE")
    while True:
        msg = c.poll(1.0)

        if msg is None:
            print('Received message is None....exiting')
            break 
            #continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print('Received message: {}'.format(msg.value().decode('utf-8')))
        print ('Value of i is - ' + str(i))
        i = i + 1
        if ( i > 10):
            break
    c.close()
    return "Confluent consumer polled COVID19 topic and successfully processed messages"

