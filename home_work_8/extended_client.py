import sys
import os
import threading
from socket import socket, AF_INET, SOCK_STREAM
from home_work_6.errors import *
from home_work_6.jim.config import *
from home_work_6.jim.utils import send_message, get_message
from home_work_6.client_log_config import logger
from home_work_6.decorator import log

sys.path.insert(0, os.getcwd())

@log
def translate_message(response):
    if not isinstance(response, dict):
        logger.error("translate_message Type error")
        raise TypeError
    if RESPONSE not in response:
        logger.error("translate_message Mandatory Key Error")
        raise MandatoryKeyError(RESPONSE)
    code = response[RESPONSE]
    if len(str(code)) != 3:
        logger.error("translate_message Response Code Length Error")
        raise ResponseCodeLenError(code)
    if code not in RESPONSE_CODES:
        logger.error("translate_message Response code error")
        raise ResponseCodeError(code)
    return response

def read_messages(client):
    while True:
        try:
            client, addr = client.accept()
            message = get_message(client)
            print(message)
        except OSError as e:
            pass

@log
def main():
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        logger.warning("Server address is empty, using localhost")
        addr = 'localhost'
    try:
        r_port = int(sys.argv[2])
    except IndexError:
        logger.warning("Server port is empty, using 7777")
        r_port = 7776
    except ValueError:
        logger.error('Port should be an integer number')
        client.close()
        sys.exit(0)
    try:
        w_port = int(sys.argv[3])
    except IndexError:
        logger.warning("Server port is empty, using 7777")
        w_port = 7777
    except ValueError:
        logger.error('Port should be an integer number')
        client.close()
        sys.exit(0)
    try:
        message = sys.argv[4]
    except IndexError:
        logger.warning("Message is empty, sending nothing")
        message = False

    client_read = socket(AF_INET, SOCK_STREAM)
    client_read.bind(('', r_port))
    client_read.listen(15)
    print("run2")
    th1 = threading.Thread(target=read_messages, args=(client_read,))
    th1.start()

    if message:
        logger.debug("Starting connection...")
        client.connect((addr, w_port))
        send_message(client, {'message': message})
        logger.debug("Waiting for response...")
        response = get_message(client)
        if response:
            response = translate_message(response)
            logger.info('Response: ' + str(response))

if __name__ == '__main__':
    logger.info("Client started")
    try:
        main()
    except Exception as e:
        logger.error("Exception: {}".format(str(e)))

    logger.info("Client stopped")
