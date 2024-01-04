import logging
import os


def setup_logger():
    LOG_REQUESTS = os.getenv("LOG_REQUESTS", 'False').lower() in ('true', '1', 't')
    DEBUG_ENABLED = os.getenv("FLASK_DEBUG", 'False').lower() in ('true', '1', 't')

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
