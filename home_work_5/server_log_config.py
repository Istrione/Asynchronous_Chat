import logging

serv_logger = logging.getLogger('server')

formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s ")

fh = logging.FileHandler("log/server.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

serv_logger.addHandler(fh)
serv_logger.setLevel(logging.DEBUG)