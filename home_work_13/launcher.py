import os
import random
import subprocess
import time

process = []

def get_name(i):
    return  f'{random.getrandbits(128)}/{i}'

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':

        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
        process.append(subprocess.Popen('gnome-terminal -- python3 server.py', shell=True))

        time.sleep(0.5)
        for i in range(clients_count):
            name = get_name(i)
            process.append(subprocess.Popen(f'gnome-terminal -- python3 client.py -n Test{name}', shell=True))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()
            victim.terminate()