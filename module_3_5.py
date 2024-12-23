def get_multiplied_digits(number):
    str_number = str(number)  # Преобразование числа в строку для работы с цифрами

    # Проверяю на окончание параметра number, если в конце ноль, то убираю ноль
    if int(str_number[-1]) == 0:
        str_number = str_number.rstrip("0")
        # print(f'проверка метода .rstrip("0") {str_number}')

    if len(str_number) > 1:
        first = int(str_number[0])  # Первая цифра в числовом представлении
        # Рекурсивный вызов функции для оставшихся цифр
        if int(str_number[-1]) != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась одна цифра, возвращаем ее
        return int(str_number[0])


# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)
result_2 = get_multiplied_digits(402030)
print(result_2)
