import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from home_work_3.jim.utils import get_message, send_message
from home_work_3.jim.config import *


def message_response(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and isinstance(message[TIME], float):
        return {RESPONSE: 200}
    else:
        return {RESPONSE: 400, ERROR: 'Incorrect request'}


def main():
    global server
    global client
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = ''

    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Port should be an integer number')
        sys.exit(0)

    # no conflicts if you rerun it
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((addr, port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        message = get_message(client)
        print(message)
        response = message_response(message)
        send_message(client, response)
        client.close()


if __name__ == '__main__':
    main()