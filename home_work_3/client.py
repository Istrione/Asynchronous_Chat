import sys
import time

from socket import socket, AF_INET, SOCK_STREAM
from home_work_3.errors import *
from home_work_3.jim.config import *
from home_work_3.jim.utils import send_message, get_message


def create_message(account_name=DEFAULT_ACCOUNT_NAME):
    if not isinstance(account_name, str):
        raise TypeError
    if len(account_name) > 25:
        raise UsernameToLongError(account_name)
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return message


def translate_message(response):
    if not isinstance(response, dict):
        raise TypeError
    if RESPONSE not in response:
        raise MandatoryKeyError(RESPONSE)
    code = response[RESPONSE]
    if len(str(code)) != 3:
        raise ResponseCodeLenError(code)
    if code not in RESPONSE_CODES:
        raise ResponseCodeError(code)
    return response


def main():
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Port should be an integer number')
        client.close()
        sys.exit(0)
    client.connect((addr, port))
    message = create_message()
    send_message(client, message)
    response = get_message(client)
    response = translate_message(response)
    print(response)
    client.close()


if __name__ == '__main__':
    main()
