# logging_example_001.py

import logging 	
from logging.config import dictConfig
from pfctrgpackage.pfc_trg_logging_config_sample  import LOGGING_CONFIG

for k,v in LOGGING_CONFIG.items():
    print ( k)

logging.config.dictConfig (LOGGING_CONFIG)

logger = logging.getLogger(__name__)

logger.info (" INFO- First line ")
logger.debug ("DEBUG - First line ")
logger.warning ("WARNING - First line ")

