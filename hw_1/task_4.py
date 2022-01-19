"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

def encode(collection):
    lst = []
    for element in collection:
        element = element.encode('utf-8')
        lst.append(element)
    return lst

def decode(collection):
    lst = []
    for element in collection:
        element = element.decode('utf-8')
        lst.append(element)
    return lst

enc = encode(words)
print(*enc, sep='\n')
print()
dec = decode(enc)
print(*dec, sep='\n')