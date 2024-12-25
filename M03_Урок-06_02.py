# ''' примеры работы с функцией any() '''
# a = [True, False, False]
# print(any(a)) # если хоть один из элементов списка True, то вернет True
# b = [False, False, False]
# print(any(b))
#
# a = [1, 0, 0]
# print(any(a)) # если хоть один из элементов списка 1, то вернет True
# b = [0, 0, 0]
# print(any(b))
#
# a = '0'
# print(any(a)) # если хоть один символ в строке есть, то вернет True
# b = ''
# print(any(b))

# ''' примеры работы с функцией all() '''
# a = [0, 1, 0]
# print(all(a))  # если все элементы списка True, то вернет True
# b = [1, 4, 2]
# print(all(b))

''' функции интроспекции'''
a = [0, 1, 0]
b = ''
# print(dir(a))
# print(type(b))
print(isinstance(b, str))  # сравнивает тип объекта на соответствие
print(type(b) == str)  # можно и так проверить соответствие

d = [1, 2, 3]
print(help(d))
