def get_multiplied_digits(number):
    str_number = str(number) # Преобразование числа в строку для работы с цифрами
    first = int(str_number[0]) # Первая цифра в числовом представлении
    # print(first, type(first))
    # print(len(str_number))
    if len(str_number) > 1:
        # Рекурсия этой функции для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Возвращаем, если осталась одна цифра
        return int(str_number[0])


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
