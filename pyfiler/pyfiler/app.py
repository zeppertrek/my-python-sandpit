# app.py 

# Logging module - similar to Log4J 
# Logging in an application is mandatory 
import os 

import logging
import logging.config

def displayOSParameters():
    print ("Current directory - ", os.getcwd())

def loadApplicationConfiguration():
    pass
	

def setLoggingConfig():
    # logging.basicConfig(format='%(message)s', level=logging.INFO)
	# This will work provided the program is executing from the correct location 
    logging.config.fileConfig(fname='pyfiler\pylogging.conf', disable_existing_loggers=False)
	
    # Get the logger specified in the file
	# What is the relevance of this statement below  ? 
    logger = logging.getLogger(__name__)
    print ("Inside setLoggingConfig")

def run():
    displayOSParameters()
	loadApplicationConfiguration()
    setLoggingConfig()
    logging.info('Start of the main routine ')
	
    #with open("solr-data", "r") as sf:  
    #sf.write("Hello World!!!")  
	
    print ("Executing app.run")
#if __name__== "__main__":
#    run()