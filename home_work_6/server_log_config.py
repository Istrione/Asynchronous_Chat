import logging
from logging.handlers import TimedRotatingFileHandler

serv_logger = logging.getLogger('server')

formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s ")

fh = TimedRotatingFileHandler("log/server.log",
                              when='midnight',
                              backupCount=5,
                              encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

serv_logger.addHandler(fh)
serv_logger.setLevel(logging.DEBUG)