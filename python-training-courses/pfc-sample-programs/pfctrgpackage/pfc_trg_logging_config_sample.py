# pfc_trg_logging_config_sample.py
# SPAR PFC training material 
# This file will define the logging configuration for the Sample program  
# 

import os

app_dir = os.path.abspath(os.path.dirname(__file__))
pfc_trg_log_file_name = app_dir + "/pfc_trg_logs.txt" 

# Note - this is a dictionary 


LOGGING_CONFIG  = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': pfc_trg_log_file_name,
            'mode' : 'w'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    },
}


#
# disable_existing_loggers 
# 1.formatters
#
#
# 2. handlers 
#
#
# 3. loggers  
#
#
#
#
SUPER_DUPER_LOG_CONFIG  = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': pfc_trg_log_file_name,
            'mode' : 'w'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    },
}