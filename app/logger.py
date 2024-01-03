import logging
# from logging import StreamHandler


def setup_logger():
    logging.basicConfig(
        format='%(asctime)s %(module)-10s %(levelname)-8s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)

    logger = logging.getLogger(__name__)

    # Add werkzeug logs to custom logger
    # werkzeug_logger = logging.getLogger('werkzeug')
    # werkzeug_logger.addHandler(handler)
    # werkzeug_logger.propagate = False

    return logger
