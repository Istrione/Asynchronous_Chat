import locale
import subprocess

#Задание №1 Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
#и содержание соответствующих переменных.
#Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип
#и содержимое переменных.

print("part 1")
word1 = "разработка"
word2 = "сокет"
word3 = "декоратор"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)

word1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
word2 = "\u0441\u043e\u043a\u0435\u0442"
word3 = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)
print('\n')

#Задание №2 Каждое из слов «class», «function», «method» записать в байтовом типе
#без преобразования в последовательность кодов (не используя методы encode
# и decode) и определить тип, содержимое и длину соответствующих переменных.

print("part 2")
word1 = b"class"
word2 = b"function"
word3 = b"method"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)
print(len(word1), len(word2), len(word3))
print('\n')

#Задание №3 Определить, какие из слов «attribute», «класс», «функция», «type»
#невозможно записать в байтовом типе.

print("part 3")
word1 = b"attribute"
word2 = "класс".encode('utf-8')  # без encode кириллицу записать нельзя
word3 = "функция".encode('utf-8')
word4 = b"type"

print(word1, word2, word3, word4)
print('\n')

#Задание №4 Преобразовать слова «разработка», «администрирование», «protocol»,
#«standard» из строкового представления в байтовое и выполнить обратное
#преобразование (используя методы encode и decode).

print("part 4")
word1 = "разработка".encode('utf-8')  # без encode кириллицу записать нельзя
word2 = "администрирование".encode('utf-8')
word3 = "protocol".encode('utf-8')
word4 = "standard".encode('utf-8')
print(word1, word2, word3, word4)
word1 = word1.decode('utf-8')
word2 = word2.decode('utf-8')
word3 = word3.decode('utf-8')
word4 = word4.decode('utf-8')
print(word1, word2, word3, word4)
print('\n')

#Задание №5 Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
#результаты из байтовового в строковый тип на кириллице.

print("part 5")

# import subprocess добавлено вверху

args1 = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']

subproc_ping = subprocess.Popen(args1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8'), end='')

subproc_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8'), end='')


#Задание №6 Создать текстовый файл test_file.txt, заполнить его тремя строками:
#«сетевое программирование», «сокет», «декоратор». Проверить кодировку
#файла по умолчанию. Принудительно открыть файл в формате Unicode и
#вывести его содержимое.

print("part 6")

# кодировка ЛОКАЛИ по умолчанию
print(locale.getpreferredencoding())

file = open("test_file.txt", "w")
file.write("сетевое программирование\n")
file.write("сокет\n")
file.write("декоратор\n")
# кодировка ФАЙЛА по умолчанию
print(file.encoding)
file.close()

with open("test_file.txt", encoding='utf-8') as file:
    for line in file:
        print(line, end='')