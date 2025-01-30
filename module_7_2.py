def custom_write(file_name, strings):
    strings_positions = {}                              # создал словарь

    file = open(file_name, 'w', encoding='utf-8')       # открываю файл для записи ('w')
    for index, strings in enumerate(strings, start=1):  # перебираю по индексу, строка в списке строк (первая строка = 1)
        byte_start = file.tell()                        # определяю позицию куросра перед записью строки в файл
        file.write(f'{strings}\n')                      # записываю строку в файл из списка строк (переменная 'info')
        strings_positions[index, byte_start] = strings  # сохранаю позицию и строку в словаре
        # print(file.closed)
    return strings_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('m07_dz-02.txt', info)
for elem in result.items():
    print(elem)