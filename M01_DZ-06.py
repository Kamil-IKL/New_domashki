my_string = input('Введите Фамилию, Имя, Отчество и дату рождения: ')
count_of_symbols = len(my_string)
print('Количество символов в Вашей строке = ', count_of_symbols)

print(my_string.upper(),' - верхний регистр')
print(my_string.lower(), ' - нижний регистр')
print(my_string.replace(' ', ""), ' - строка без пробелов')
print(my_string[0], ' - первый символ строки')
print(my_string[-1], ' - последний символ строки')