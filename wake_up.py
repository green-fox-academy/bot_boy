import logging
import client_service

logger = logging.getLogger('bot_application')
logger.setLevel(logging.DEBUG)
logger.info('app running')
client_service.start()
