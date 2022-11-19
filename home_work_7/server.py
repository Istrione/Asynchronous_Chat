import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from home_work_6.jim.utils import get_message, send_message
from home_work_6.jim.config import *

from home_work_6.server_log_config import serv_logger
from home_work_6.decorator import log

import select


def read_requests(r_clients, all_clients):
    messages = []
    for sock in r_clients:
        try:
            message = get_message(sock)
            messages.append(message)
        except:
            print('Client {} {} disconnected'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return messages


def write_responses(messages, w_clients, all_clients):
    for sock in w_clients:
        for message in messages:
            try:
                response = message_response(message)
                send_message(sock, response)
            except:
                print('Client {} {} disconnected'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

@log
def message_response(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and isinstance(message[TIME], float):
        serv_logger.debug("message_response correct request")
        return {RESPONSE: 200}
    else:
        serv_logger.error("message_response Incorrect request")
        return {RESPONSE: 400, ERROR: 'Incorrect request'}


@log
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

    # no conflicts if you rerun it
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serv_logger.debug("Starting connection...")
    server.bind((addr, port))
    server.listen(15)
    server.settimeout(0.2)
    clients = []
    while True:
        try:
            serv_logger.debug("Accepting...")
            client, addr = server.accept()
        except OSError as e:
            pass
        else:
            clients.append(client)
        finally:
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


if __name__ == '__main__':
    serv_logger.info("Server started")
    try:
        main()
    except Exception as e:
        serv_logger.error("Exception: {}".format(str(e)))
    serv_logger.info("Server stopped")