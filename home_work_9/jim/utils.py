import json

ENCODING = 'utf-8'


def dict_to_bytes(message_dict):
    if isinstance(message_dict, dict):
        jmessage = json.dumps(message_dict)
        bmessage = jmessage.encode(ENCODING)
        return bmessage
    else:
        raise TypeError


def bytes_to_dict(message_bytes):
    if isinstance(message_bytes, bytes):
        jmessage = message_bytes.decode(ENCODING)
        message = json.loads(jmessage)
        if isinstance(message, dict):
            return message
        else:
            raise TypeError
    else:
        raise TypeError


def send_message(sock, message):
    bpresence = dict_to_bytes(message)
    sock.send(bpresence)


def get_message(sock):
    bresponse = sock.recv(1024)
    response = bytes_to_dict(bresponse)
    return response