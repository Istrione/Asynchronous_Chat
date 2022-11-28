import sys
import time

from socket import socket, AF_INET, SOCK_STREAM
from home_work_6.errors import *
from home_work_6.jim.config import *
from home_work_6.jim.utils import send_message, get_message
from home_work_6.client_log_config import logger
from home_work_6.decorator import log


@log
def create_message(account_name=DEFAULT_ACCOUNT_NAME):
    if not isinstance(account_name, str):
        logger.warning("create_message Type Error")
        raise TypeError
    if len(account_name) > 25:
        logger.warning("create_message Username Too Long Error")
        raise UsernameTooLongError(account_name)
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return message

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

@log
def main():
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        logger.warning("Server address is empty, using localhost")
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        logger.warning("Server port is empty, using 7777")
        port = 7777
    except ValueError:
        logger.error('Port should be an integer number')
        client.close()
        sys.exit(0)
    logger.debug("Starting connection...")
    client.connect((addr, port))
    message = create_message()
    logger.debug("Sending message...")
    send_message(client, message)
    logger.debug("Waiting for response...")
    response = get_message(client)
    response = translate_message(response)
    logger.info('Response: ' + str(response))
    client.close()


if __name__ == '__main__':
    logger.info("Client started")
    try:
        main()
    except Exception as e:
        logger.error("Exception: {}".format(str(e)))

    logger.info("Client stopped")
