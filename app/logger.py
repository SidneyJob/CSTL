import logging
import os


def check_decision(environment_variable: str, default_value: str) -> bool: 
    '''Checks if environment variable is True OR False'''
    decision = os.getenv(environment_variable, default_value).lower() in ['true', 't', '1']

    return decision


def setup_logger():
    LOG_REQUESTS = check_decision("LOG_REQUESTS", 'False')
    DEBUG_ENABLED = check_decision("FLASK_DEBUG", 'False')

    if DEBUG_ENABLED:
        LOG_LEVEL = "DEBUG"
    else:
        LOG_LEVEL = "INFO"

    # LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()

    logging.basicConfig(
        format='%(asctime)s %(module)-10s %(levelname)-8s %(message)s',
        datefmt='%H:%M:%S',
        level=LOG_LEVEL)

    logger = logging.getLogger(__name__)

    # Disable werkzeug logs to custom logger
    # if env variable LOG_REQUESTS = False
    if not bool(LOG_REQUESTS):
        werkzeug_logger = logging.getLogger('werkzeug')
        werkzeug_logger.disabled = True

    return logger
