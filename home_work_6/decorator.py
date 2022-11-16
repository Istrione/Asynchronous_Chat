from home_work_6.client_log_config import logger
from functools import wraps
import inspect


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug('Function {} was called from {}'.format(func.__name__, inspect.stack()[1][3]))
        logger.debug('Function {}({}, {}), return {}'.format(func.__name__, args, kwargs, res))
        return res
    return call
