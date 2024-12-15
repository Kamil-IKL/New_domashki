# ''' бесконечный цикл '''
# while 1 > 0: # True
#     number = int(input('Enter a number: '))
#     if number % 2 == 0:
#         print('Число четное')
#     else:
#         print('Число нечетное')
# print('Я за циклом')

# ''' цикл прерывается, если число нечетное (используем оператор "break") '''
# while True: # True
#     number = int(input('Enter a number: '))
#     if number % 2 == 0:
#         print('Число четное')
#     else:
#         print('Число нечетное')
#         break
# print('Я за циклом')

''' цикл непрерывается, используем оператор "continue" '''
while 1 > 0: # True
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        print('Число четное')
        continue
    else:
        print('Число нечетное')
    print('Меня не забыли')
print('Я за циклом')