"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']

def info(collection):
    for element in collection:
        try:
            print(bytes(element, 'ascii'))
        except UnicodeEncodeError:
            print(f"'{element}' - невозможно записать в виде байтовой строки")

info(words)
