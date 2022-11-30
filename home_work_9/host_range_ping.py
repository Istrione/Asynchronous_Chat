# Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.

import ipaddress
import socket

from home_work_9.host_ping import host_ping


def host_range_ping(adress):
        result=[]
        list_octets = str(ipaddress.ip_address(socket.gethostbyname(adress))).split('.')
        last_octet = list_octets[3]
        for item in range(1, int(last_octet) + 1):
            dict_result_for_adress = {}
            list_octets[-1] = str(item)
            changed_octet_ip = '.'.join(list_octets)
            status = host_ping(changed_octet_ip)
            dict_result_for_adress["Узел"] = changed_octet_ip
            dict_result_for_adress["Статус"] = status
            result.append(dict_result_for_adress)
        return result


if __name__ == '__main__':
    host = 'www.mail.ru'
    host_range_ping(host)