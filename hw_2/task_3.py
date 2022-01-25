"""
3. Задание на закрепление знаний по модулю yaml. 
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, 
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке 
ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с 
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

data_to_yaml = {
    'first_a': ['msg_1', 'msg_2', 'msg_3'],
    'first_b': 10,
    'first_c': {'second_a': '20€'}
}

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data_to_yaml, f_in, default_flow_style=True, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as f_out:
    yaml_to_data = yaml.load(f_out, Loader=yaml.SafeLoader)

print(data_to_yaml == yaml_to_data)
