# Docker File Name - Dockerfile
# Author : Sanjiv Nagraj
# Dockerizing a Python 3.7, Flask web application 
# 14/01/2020 - 17:30 - Created my first docker file 
# docker build -t vm_docker_flask .
# 

# We've skipped the Ubuntu bit 
FROM python:3.7.3

LABEL Author="Zepper Trekker"
LABEL E-mail="zeppertrek@gmail.com"
LABEL version="ZT01.01"

#ENV PYTHONDONTWRITEBYTECODE 1

ENV FLASK_APP "main.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir /ztdemoapp
# We copy just the requirements.txt first to leverage Docker cache - Need to understand

COPY ./requirements.txt /ztdemoapp/requirements.txt

WORKDIR /ztdemoapp 


# As this is an isolated environment, there is no need to create a virtual environment 
# pip - Python 2 ?



RUN pip3 install -r requirements.txt

COPY . /ztdemoapp

EXPOSE 8041
#EXPOSE 5000

# Using Flask's inbuilt WSGI server OR Waitress 
CMD waitress-serve --port=8041 --host 0.0.0.0  main:app
#CMD flask run --host=0.0.0.0






