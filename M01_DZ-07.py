immutable_var = ('Петров', 25, 'man',  True, 120)
print(immutable_var, type(immutable_var))

# попытка изменить кортеж
# immutable_var[0] = 'Иванов'
# print(immutable_var)
# выдает ошибку ... кортеж не поддерживает изменение значений элементов, однако, еслу внутри кортежа есть элемент
# в виде списка, то сам спиcок внутри кортежа можно изменить (см. пример)
immutable_var = (['Петров Валерий Тимофеевич'], 25, 'man',  True, 120)
print(immutable_var, type(immutable_var))
print(immutable_var[0])
immutable_var[0] [0] = 'Сидоренко Фурхат Кимович'
print(immutable_var, type(immutable_var))

# возможные операции с кортежом
immutable_var = immutable_var * 2
print(immutable_var, type(immutable_var))

# добавление элемента в кортеж, путем сложения кортежей
immutable_var = immutable_var + ('student', )
print(immutable_var, type(immutable_var))

# изменение элемента в списке
mutable_list = ['Петров', 25, 'man',  True, 120]
print(mutable_list, type(mutable_list))
mutable_list[0] = 'Иванов'
print(mutable_list)


