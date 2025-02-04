def personal_sum(numbers):
    '''
    Подсчитывает сумму чисел в коллекции и количество некорректных данных.
    :param numbers: коллекция в виде кортежа или списка
    :return: кортеж из суммы чисел и кол-ва некорректных данных
    '''
    result = 0  # создаем переменную суммы чисел
    incorrect_data = 0  # создаем счетчик некорректных данных

    try:
        for number in numbers:
            try:
                result += float(number)  # приводим к числу и увеличиваем
            except (TypeError, ValueError) as exc:
                print(f'перехват ошибки: {exc}')
                incorrect_data += 1  # увеличиваем счетчик некорректных данных
        return round(result, 2), incorrect_data  # возвращаем с округлением до двух знаков

    except TypeError as exc:  # перехват ошибки в случае numbers == строка
        print(f'перехват ошибки: {exc}')
        return


def calculate_average(numbers):
    '''
    Подсчитывает среднее арифметическое чисел коллекции
    :param numbers: коллекция в виде кортежа или списка
    :return: среднее арифметическое всех чисел коллекции
    '''
    try:
        result, incorrect_data = personal_sum(numbers)  # распаковываем кортеж значения из функции personal_sum
        count = len(numbers) - incorrect_data  # счетчик корректных данных
        return result / count  # возвращаем среднее арифметическое

    except (TypeError, ZeroDivisionError) as exc:
        print(f'перехват ошибки: {exc}')
    return 0


# # проверка функции personal_sum
# print(personal_sum([1.9, '2.5', '4']))
# print(personal_sum([1.9, '2.5', 'four']))
# print(personal_sum(('1, 2, 3')))
# print(personal_sum((567)))


# проверка функции calculate_average
print(f'Результат 0: {calculate_average(("one, two, three"))}\n')  # Строка перебирается,  чисел нет
print(f'Результат 1: {calculate_average("1, 2, 3")}\n')  # Строка перебирается, но числа переводятся в числовой тип
print(f'Результат 2: {calculate_average([2, "Строка", 3, "Ещё Строка"])}\n')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}\n')  # Передана не коллекция
print(f'Результат 4: {calculate_average((567,))}\n')  # Передана коллекция из одного числа
print(f'Результат 5: {calculate_average([42, 15, 36, 13])}\n')  # Всё должно работать

# print(personal_sum(('я это сделал')))
# print(f'Результат 0: {calculate_average(('я это сделал'))}\n')
