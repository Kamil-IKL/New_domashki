# name = input('Введите Ваше имя: ')
# if name == 'Urban':
#     print('Здравствуйте, администратор')
# if name == 'Камиль':
#     print('Здравствуйте, студент', name)
# else:
#     print('Привет,', name)

# ''' Программка на выполнение условий, но не совсем корректно выполняется при условии 15'''
# number = int(input('Введите число: '))      # Fizz, Buzz, FizzBuzz
# if number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# elif number % 3 == 0 and number % 5 == 0:     # or - "или"; and - "и"
#     print('FizzBuzz')

''' Программка на выполнение условий, правильная '''
number = int(input('Введите число: '))      # Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:     # or - "или"("нестрогий" оператор); and - "и"("строгий" оператор)
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число не подходит')

