first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Введено 3 равных числа')
elif first == second or first == third or second == third:
    print('Вы ввели 2 одинаковых числа')
else:
    print('Одинаковых чисел - ', 0)
