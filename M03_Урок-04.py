# def test_func(*params):
#     print('Тип:', type(params))
#     print('Аргумент:', params)
#     pass
#
#
# test_func(1, 2, 3, 4)


# def summator(*values):
#     s = 0
#     for i in values:
#         s += i
#     return s
#
#
# print(summator(1, 2, 3, 4))


# def summator(txt, *values):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s}'
#
#
# print(summator('Сумма чисел: ', 2, 3, 4))


# def summator(txt, *values, type='sum'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
# print(summator('Сумма чисел: ', 2, 3, 4))

# def summator(txt, *values, type='summator'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
# print(summator('Сумма чисел: ', 2, 3, 4))


# ''' в данном случае создается словарь при передаче параметров функции '''
# def info(**values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#
# info(name='Denis', course='Python')

#
# ''' используем цикл for и метод .items для приведения в удобочитаемый вид '''
# def info(**values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#     for key, values in values.items():
#         print(key, values)
#
# info(name='Denis', course='Python')
#
# def info(*types, **values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#     for key, values in values.items():
#         print(key, values)
#     print(types)
#
#
# info(1,2,3,4, name='Denis', course='Python')

# def info(value, *types, names_author='Den', **values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#     for key, values in values.items():
#         print(key, values)
#     print(types)
#
#
# info('Пример использования параметров всех типов', 2, 3, 4, names_author='Denis', name='Den', course='Python')

'''Пример функции для нахождения суммы чисел, а также квадратов, кубов и т.д.'''
def my_sum(n, *args, txt='Сумма чисел'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ':', s)


my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt='Сумма квадратов')

