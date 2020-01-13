# Docker File Name - Dockerfile
# Author : Sanjiv Nagraj
# Dockerizing a Python 3.7, Flask web application 
# 13/01/2020 - 17:30 - Created my first docker file 


# Investigate this image using another project  
# FROM python:3.7.3


#############################################################################
# What does label do ? 
#LABEL Author="ZT"
#LABEL E-mail="zeppertrek@gmail.com"
#LABEL version="0.1"
# What does ENV PYTHONDONTWRITEBYTECODE 1 do ? 
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV FLASK_APP "backend/app.py"
#ENV FLASK_ENV "development"
# ENV FLASK_DEBUG True
#RUN mkdir /app
#WORKDIR /app
#COPY Pip* /app/
#
# Difference between ADD and COPY 
################################################################################

#MAINTAINER Zepper Trek "zeppertrek@gmail.com"


FROM ubuntu:18.04


RUN apt-get update -y 

RUN apt-get install python3.7 -y

RUN apt-get install python3-pip  -y 

RUN apt-get install python3.7-venv  -y 



###############################################################################################
# Review stuff below 
# We copy just the requirements.txt first to leverage Docker cache


ENV FLASK_APP "main.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
#


RUN mkdir /spardemoapp


# We copy just the requirements.txt first to leverage Docker cache - Need to understand
COPY ./requirements.txt /spardemoapp/requirements.txt

WORKDIR /spardemoapp

# As this is an isolated environment, there is no need to create a virtual environment 
# pip - Python 2 ?
RUN pip3 install -r requirements.txt

COPY . /spardemoapp

#ENTRYPOINT [ "python" ]
#CMD [ "main.py" ]

EXPOSE 5000


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Can this be 127.0.0.1 ?
CMD flask run --host=0.0.0.0