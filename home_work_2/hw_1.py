import csv
import re

#Задание №1 Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
#данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.

def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for file_name in file_list:
        with open(file_name, encoding='cp1251') as f_n:
            for row in f_n:
                param = re.split(":\s+", row.strip())
                if isinstance(param, list) and len(param) == 2:
                    if param[0] == 'Изготовитель системы':
                        os_prod_list.append(param[1])
                    elif param[0] == 'Название ОС':
                        os_name_list.append(param[1])
                    elif param[0] == 'Код продукта':
                        os_code_list.append(param[1])
                    elif param[0] == 'Тип системы':
                        os_type_list.append(param[1])
    header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    return header, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv():
    data = get_data()
    number_of_lines = len(data[1])
    processed_data = [data[0]]
    for i in range(number_of_lines):
        processed_data.append([row[i] for row in data[1:]])
    with open('info_result.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        for row in processed_data:
            f_n_writer.writerow(row)


if __name__ == '__main__':
    write_to_csv()