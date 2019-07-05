# pyfiler.py 

# Logging module - similar to Log4J 
import logging

import logging.config


def setLoggingConfig():
    # logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.config.fileConfig(fname='pylogging.conf', disable_existing_loggers=False)

def main():
    setLoggingConfig()
    logging.info('Start of the main routine ')

if __name__== "__main__":
    main()