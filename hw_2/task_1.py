"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в
него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import re
import csv
from chardet import detect

def enc_type(file):
    with open(file, 'rb') as fl:
        ENCODING = detect(fl.read())['encoding']
        return ENCODING

def get_data(files):
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in files:
        with open(file, 'r', encoding=enc_type(file)) as f_n:
            data = f_n.read()
            pattern = re.compile(r'Изготовитель системы:\s*.*')
            os_prod_list.append(' '.join(pattern.findall(data)[0].split()[2:]))
            pattern = re.compile(r'Название ОС:\s*.*')
            os_name_list.append(' '.join(pattern.findall(data)[0].split()[2:]))
            pattern = re.compile(r'Код продукта:\s*.*')
            os_code_list.append(' '.join(pattern.findall(data)[0].split()[2:]))
            pattern = re.compile(r'Тип системы:\s*.*')
            os_type_list.append(' '.join(pattern.findall(data)[0].split()[2:]))
    number_list = [number for number in range(1, 4)]
    main_data = [[row[n] for row in [number_list, os_prod_list, os_name_list, os_code_list, os_type_list]] for n in range(3)]
    main_data.insert(0, headers)
    return main_data

def write_to_csv(file):
    with open(file, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        data = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
        for row in data:
            f_n_writer.writerow(row)

write_to_csv('task_1_csv.csv')

with open('test.csv', encoding='utf-8') as f_n:
    print(f_n.read())

