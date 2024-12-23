def get_multiplied_digits(number):
    str_number = str(number) # Преобразование числа в строку для работы с цифрами
    first = int(str_number[0]) # Первая цифра в числовом представлении
    # print(first, type(first))
    # print(len(str_number))
    
    # Проверяю на окончание параметра number, если в конце ноль, то убираю ноль
    if int(str_number[-1]) == 0:
        str_number = str_number.rstrip("0")
        # print(f'проверка метода .rstrip("0") {str_number}')
    
    if len(str_number) > 1:
        # Рекурсия этой функции для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Возвращаю, если осталась одна цифра
        return int(str_number[0])


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
