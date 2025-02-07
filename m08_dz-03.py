class IncorrectVinNumber(Exception):
    ''' Исключение для некорректного vin номера '''

    def __init__(self, message):
        self.message = message

    pass


class IncorrectCarNumbers(Exception):
    ''' Исключение для некорректного номера автомобиля '''

    def __init__(self, message):
        self.message = message

    pass


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model  # название автомобиля
        # self.__vin = __vin  # vin номер автомобиля
        self.__vin = self.__is_valid_vin(__vin)
        # self.__numbers = __numbers  # номера автомобиля
        self.__numbers = self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        '''
        Проверяет корректность vin номера
        :param vin_number: int(число)
        :return: True
        '''
        # проверка на тип данных
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'{self.model}: некорректный тип vin номер')

        # проверка на диапазон
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber(f'{self.model}: неверный диапазон для vin номера')

        return True  # Если проверки пройдены, возвращает True

    def __is_valid_numbers(self, numbers):
        '''
        Проверяет корректность номера автомобиля
        :param numbers: str(строка)
        :return: True
        '''
        # проверка на диапазон
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'{self.model}: некорректный тип данных для номеров')

        # проверка на длину номера
        if not (len(numbers) == 6):
            raise IncorrectCarNumbers(f'{self.model}: неверная длина номера')

        return True  # Если проверки пройдены, возвращает True


# проверка работы кода
try:
    first = Car('Model1 "Ferrari"', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2 "Запорожец"', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3 "Moskvich"', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
