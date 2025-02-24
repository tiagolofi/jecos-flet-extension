import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format = '[%(levelname)s] %(asctime)s: %(pathname)s > %(module)s > %(funcName)s > %(lineno)d: %(message)s'
)
log = logging.getLogger(__name__)
