''' Работа со словарями '''
my_dict = {'Denis': 1989, 'Tanya': 1977, 'Radik': 1966, 'Ruslan': 1990}
print(my_dict)

# вытаскиваю значение по ключу
print(my_dict['Radik'])
print(my_dict.get('Lusya')) # чтобы не выдавало ошибку

# добавляю несколько элементов одновременно
my_dict.update({'Lusya': 1970,
                'Ali': 1997})
print(my_dict)

# получаю значение по ключу и сразу удаляя этот элемент из словаря
print(my_dict.pop('Tanya'))
print(my_dict)


''' Работа с множествами '''
my_set = {1, 2, 3, 4, 2, 1, 6, 4, 7, 3, 6, 3, 'Множества', True, (1, 2, 3)}
print(my_set)

# добавляю два элемента
my_set.update({10, 'год'})
print(my_set)

# удаляю элемент(кортеж) в множестве
print(my_set.remove((1, 2, 3)))
print(my_set)