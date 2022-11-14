import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from home_work_5.jim.utils import get_message, send_message
from home_work_5.jim.config import *
from home_work_5.server_log_config import serv_logger


def message_response(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and isinstance(message[TIME], float):
        serv_logger.debug("message_response correct request")
        return {RESPONSE: 200}
    else:
        serv_logger.error("message_response Incorrect request")
        return {RESPONSE: 400, ERROR: 'Incorrect request'}

def main():
    global server
    global client
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        serv_logger.warning("Client address is empty, listening to all")
        addr = ''

    try:
        port = int(sys.argv[2])
    except IndexError:
        serv_logger.warning("Listen port is empty, listening to 7777")
        port = 7777
    except ValueError:
        serv_logger.error('Port should be an integer number')
        sys.exit(0)

    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serv_logger.debug("Starting connection...")
    server.bind((addr, port))
    server.listen(1)
    while True:
        serv_logger.debug("Accepting...")
        client, addr = server.accept()
        serv_logger.debug("Get message...")
        message = get_message(client)
        serv_logger.info('Message: ' + str(message))
        response = message_response(message)
        serv_logger.debug("Sending response...")
        send_message(client, response)
        client.close()


if __name__ == '__main__':
    serv_logger.info("Server started")
    try:
        main()
    except Exception as e:
        serv_logger.error("Exception: {}".format(str(e)))
    serv_logger.info("Server stopped")