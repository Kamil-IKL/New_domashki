def calculate_structure_sum(data):
    total = 0  # создаю переменную для подсчета

    # проверка исходного списка или кортежа, с использованием метода "isinstance" для определения типа данных
    for i in data:
        if isinstance(i, (int, float)):  # проверяю, является ли элемент числом
            total += i
        elif isinstance(i, str):  # проверяю, элемент на "строка" или нет
            total += len(i)  # суммируем длину строки
        elif isinstance(i, (list, tuple, set)):  # проверяю, является ли элемент списком, кортежом или множеством
            total += calculate_structure_sum(i)  # применяю рекурсию для вложенных списков, кортежей или множеств
        elif isinstance(i, dict):  # Проверяю, является ли элемент словарем
            total += calculate_structure_sum(i.keys())  # Суммирую ключи
            total += calculate_structure_sum(i.values())  # Суммирую значения

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
