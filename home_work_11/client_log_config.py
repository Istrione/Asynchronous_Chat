import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('client')

formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s ")

fh = TimedRotatingFileHandler("log/client.log",
                              when='midnight',
                              backupCount=5,
                              encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

