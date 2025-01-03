class House:
    houses_history = []  # Атрибут класса для хранения истории домов

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # создаю новый экземпляр(объект) класса
        house_name = args[0]
        if house_name in args:
            cls.houses_history.append(house_name)
        return instance

    def __init__(self, name, number_of_floors):
        # атрибуты класса
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # метод "Лифт"
        from time import sleep  # импортирую метод задержки времени
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'\nТакого этажа не существует\n')
        else:
            for i in range(1, new_floor + 1):
                sleep(0.5)
                print(f'Вы находитесь на этаже: {i}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # перезагрузка оператора " == "
    def __eq__(self, other):
        if isinstance(other, House):  # проверяю, является ли other экземпляром класса "House"
            return self.number_of_floors == other.number_of_floors
        return False

    # перезагрузка оператора " < "
    def __lt__(self, other):
        if isinstance(other, House):  # проверяю, является ли other экземпляром класса "House"
            return self.number_of_floors < other.number_of_floors

    # перезагрузка оператора " <= "
    def __le__(self, other):
        if isinstance(other, House):  # проверяю, является ли other экземпляром класса "House"
            return self.number_of_floors <= other.number_of_floors

    # перезагрузка оператора " > "
    def __gt__(self, other):
        if isinstance(other, House):  # проверяю, является ли other экземпляром класса "House"
            return self.number_of_floors > other.number_of_floors

    # перезагрузка оператора " >= "
    def __ge__(self, other):
        if isinstance(other, House):  # проверяю, является ли other экземпляром класса "House"
            return self.number_of_floors >= other.number_of_floors

    # перезагрузка оператора " != "
    def __ne__(self, other):
        if isinstance(other, House):  # проверяю, является ли other экземпляром класса "House"
            return self.number_of_floors != other.number_of_floors

    # увеличиваю количество этажей
    def __add__(self, value):
        if isinstance(value, int):  # проверяю, является ли "value" числом
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    # перезагрузка оператора " del "
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
