calls = 0


def count_calls():
    ''' счетчик вызова функций '''
    global calls  # вызов переменной из глобального пространства
    print(calls)


def string_info(str):
    # для подсчета вызова этой функции
    global calls  # вызов переменной из глобального пространства
    calls += 1  # присваюиваем новое значение глобальной переменной при каждом вызове

    str_count = len(str)  # подсчет длины строки
    str_upper = str.upper()  # перевод строки в верхний регистр
    str_lower = str.lower()  # перевод строки в нижний регистр
    return (str_count, str_upper, str_lower)


def is_contains(str, list):
    ''' функция поиска строки(слова, имени и т.д.) в списке строк(имен) '''
    # для подсчета вызова этой функции
    global calls  # вызов переменной из глобального пространства
    calls += 1  # присваюиваем новое значение глобальной переменной при каждом вызове

    str_lower = str.lower()  # перевод аргумента функции "str" в нижний регистр
    found = False  # Переменная для отслеживания, был ли найден элемент

    # проверяю наличие строки в списке
    for i in list:
        if str_lower == i.lower():  # перевожу элемент списка в нижний регистр и сравниваю с аргументом "str"
            found = True
            # break - можно использовать, если нет необходимости перебирать весь список, т.е. если слово не повторяется.
    print(found)


print(string_info("стPOка"))
print(string_info("университет УрБАН"))
is_contains("каМиЛЬ", ['il', 'кАм', 'Kam', 'Камиль', 'KaMil'])
is_contains("Урбан", ['il', 'кАм', 'Kam', 'Камиль', 'KaMil'])
count_calls()