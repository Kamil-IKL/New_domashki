n = int(input("Введите число от 3 до 20: "))


def password_search(n):
    result = ""

    ''' создаю пары чисел от 1 до 20 '''
    for i in range(1, 21):  # перебираю первое число
        for j in range(i + 1, 21):  # перебираю второе, при этом (i + 1) это для исключения повторения
            sum_para = i + j

            if n % sum_para == 0:  # определяю кратность n сумме пары
                result += f"{i}{j}"  # формирую пару и добавляю в result

    return result


while n < 3 or n > 20:
    print("Число должно быть в диапазоне от 3 до 20.")
    break
else:
    password = password_search(n)
    print(f"Нужный пароль для числа {n}: {password}")
