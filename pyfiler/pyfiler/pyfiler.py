# app.py 

# Logging module - similar to Log4J 
# Logging in an application is mandatory 
import logging

import logging.config


def setLoggingConfig():
    # logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.config.fileConfig(fname='pylogging.conf', disable_existing_loggers=False)
	
    # Get the logger specified in the file
	# What is the relevance of this statement below  ? 
    logger = logging.getLogger(__name__)


def main():
    setLoggingConfig()
    logging.info('Start of the main routine ')
	
	with open("solr-data", "r") as sf:  
    sf.write("Hello World!!!")  
	

if __name__== "__main__":
    main()