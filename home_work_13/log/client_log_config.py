import logging
import sys

format_logger = f"%(asctime)s %(levelname)s %(name)-5s %(message)s"


def get_file_handler():
    file_handler = logging.FileHandler("client.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter(format_logger))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(format_logger))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger('app.clients')
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger

