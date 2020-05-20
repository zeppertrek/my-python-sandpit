# logging_example_002.py

import logging 	
from logging.config import dictConfig
from pfctrgpackage.pfc_trg_logging_config_sample  import SUPER_DUPER_LOG_CONFIG

for k,v in LOGGING_CONFIG.items():
    print ( k)

logging.config.dictConfig (SUPER_DUPER_LOG_CONFIG)

logger = logging.getLogger(__name__)

logger.info (" INFO- First line ")
logger.debug ("DEBUG - First line ")
logger.warning ("WARNING - First line ")

