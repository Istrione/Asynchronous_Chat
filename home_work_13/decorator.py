from functools import wraps
import logging
from inspect import currentframe, getouterframes, stack


def log(func):
    if func.__name__ == 'clients':
        logger = logging.getLogger('clients')
    else:
        logger = logging.getLogger('server')

    @wraps(func)
    def wrapper(*args, **kwargs):
        modul_name = getouterframes(currentframe())[1][3]

        logger.info(
            f'Функция с именем {func.__name__} вызвана, аргумент {args},'
            f'{kwargs}. Вызов из {modul_name}.')
        return func(*args, **kwargs)

    return wrapper