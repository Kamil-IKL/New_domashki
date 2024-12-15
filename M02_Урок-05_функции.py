''' обычная функция '''
# def say_hello():
#     print('Hello')

# say_hello()
# say_hello()
# say_hello()


''' принимающая функция'''
# def say_hello(name):
#     print('Hello', name)
#
# say_hello('Kamil')
# say_hello('Max')
# say_hello('Denis')

import random

''' возвращающая функцияw '''
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win  # возвращает значение переменной "win"
#
#
# win = lottery()
# print(win)

'''одновременное принимающая и возвращающая функция'''
# def lottery(mon, thue): # указываем два аргумента функции
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(mon, thue)
#     return win1, win2  # возвращает значение переменной "win"
#
#
# win1, win2 = lottery('mon', 'thue')
# print(win1, win2)
#
# def lottery(*args, **kwargs): # неопределнны количество аргументов функции
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2  # возвращает значение переменной "win"
#
# win1, win2 = lottery([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])
# print(win1, win2)

'''принимающая функция с значениями по умолчанию'''
def test(a=2, b=True):
    print(a, b)


test()
test(False, 'ok')
# test([1, 2])
test(*[1, 2])  # распаковка списка
test(*{'Denis': 1, 'Max': 2})  # распаковка словаря
