# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         # print(n + summa(n - 1))
#         return n + summa(n - 1)
#
#
# print(summa(5))

# stack = []
# stack.append(1)
# print('Добавили элемент', stack)
# stack.append(2)
# print('Добавили элемент', stack)
# stack.append(3)
# print('Добавили элемент', stack)

# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)

''' самая распространенная ошибка, использования рекурсии  "переполнения памяти"
    вы не предусмотрели выход из функции '''
def recursion():
    return recursion() + 1


recursion()
