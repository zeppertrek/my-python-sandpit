# app.py 

# Logging module - similar to Log4J 
# Logging in an application is mandatory 
import logging

import logging.config


def setLoggingConfig():
    # logging.basicConfig(format='%(message)s', level=logging.INFO)
	# This will work provided the program is executing from the correct location 
    #logging.config.fileConfig(fname='pylogging.conf', disable_existing_loggers=False)
	
    # Get the logger specified in the file
	# What is the relevance of this statement below  ? 
    #logger = logging.getLogger(__name__)
    print ("Inside setLoggingConfig")

def run():
    setLoggingConfig()
    logging.info('Start of the main routine ')
	
    #with open("solr-data", "r") as sf:  
    #sf.write("Hello World!!!")  
	
    print ("Executing app.run")
#if __name__== "__main__":
#    run()