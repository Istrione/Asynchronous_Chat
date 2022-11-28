# Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().

import ipaddress
import socket
import subprocess

def host_ping(host):
    adress = ipaddress.ip_address(socket.gethostbyname(host))
    code = subprocess.call(["ping", str(adress)])
    if code == 0:
        status = 'доступен'
    else:
        status = 'недоступен'

    return status

if __name__ == '__main__':
    list_ip = ['www.yandex.ru', 'www.mail.ru', 'www.google.com', '198.168.1.12', '100.2.15.3', '5.5.5.5']
    for item in list_ip:
        stat = host_ping(item)
        print(f'Узел {item} {stat}')