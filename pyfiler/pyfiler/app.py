# app.py
# Use functions / function decorators, data structures, exception handling, classes, iteration extensively
# Try to use multi threading    

# Logging module - similar to Log4J 
# Logging in an application is mandatory 
import logging

import logging.config

def displayOSParameters():
    pass

def loadConfigParameters():
    pass 

def processDataFromCSVFiles()
    pass

def insertDataIntoMongoDB()
    pass

def insertDataIntoSOLR()
    pass

def insertDataIntoKafka()
    pass

def insertDataIntoRedis()
    pass
#
def insertDataIntoPostGreSQL()
    pass 	


def setLoggingConfig():
    # logging.basicConfig(format='%(message)s', level=logging.INFO)
	# This will work provided the program is executing from the correct location 
    #logging.config.fileConfig(fname='pylogging.conf', disable_existing_loggers=False)
	
    # Get the logger specified in the file
	# What is the relevance of this statement below  ? 
    #logger = logging.getLogger(__name__)
    print ("Inside setLoggingConfig")

def run():
    #Display OS level parameters. Demonstrates the use of  Python's extensive standard library
    displayOSParameters()
    # will read from config.json 
	# config.json should never be checked into GIT.  Instead config.json.example should be checked in 
    loadConfigParameters()
    # Make sure that logs are being generated correctly 
	# Configuring application level logging is the most important thing that you can do 
    setLoggingConfig()
    logging.info('Start of the main routine ')
	
    #with open("solr-data", "r") as sf:  
    #sf.write("Hello World!!!")  
	
    print ("Executing app.run")
	
	# 
	processDataFromCSVFiles()
	#
	insertDataIntoMongoDB()
	#
	insertDataIntoSOLR()
	#
	insertDataIntoKafka()
	#
	insertDataIntoRedis()
	#
	insertDataIntoPostGreSQL()
	
	
#if __name__== "__main__":
#    run()