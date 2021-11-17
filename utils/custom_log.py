import logging
import coloredlogs

"""
Custom logger to print colored messages to seperate info, error and success messages.
"""

logger = logging.getLogger("vendingmachine")
coloredlogs.install(level=logging.DEBUG, logger=logger, fmt='%(message)s')

MSG_INFO = 'INFO'
MSG_DEBUG = 'SUCCESS'
MSG_ERROR = 'ERROR'

logger_types = {'INFO': logger.info, 'SUCCESS': logger.debug, 'ERROR': logger.error}


def custom_log(msg_text, msg_type):

    if msg_type not in logger_types:
        raise ValueErro("Message type not found.")

    logger_type = logger_types[msg_type]
    logger_type(msg_text)
