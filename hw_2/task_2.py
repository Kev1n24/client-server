"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл 
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json

def write_order_to_json(item, quantity, price, buyer, date):
    
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    
    with open('orders.json',  encoding='utf-8') as f_in:
        objs = json.load(f_in)

    with open('orders.json', 'w',  encoding='utf-8') as f_out:
        objs['orders'].append(dict_to_json)
        f_out.write(json.dumps(objs, sort_keys=True, indent=4))


write_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')

with open('orders.json') as f_n:
    print(f_n.read())
