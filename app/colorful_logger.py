import os
import logging
import colorlog

logger_name = "lab_logger"


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

    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s %(levelname)-8s %(module)-10s %(message)s',
        datefmt='%H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(color_formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)
    logger.propagate = False

    logger.addHandler(console_handler)

    # Disable werkzeug logs to custom logger
    # if env variable LOG_REQUESTS = False
    if not bool(LOG_REQUESTS):
        werkzeug_logger = logging.getLogger('werkzeug')
        werkzeug_logger.disabled = True

    return logger
