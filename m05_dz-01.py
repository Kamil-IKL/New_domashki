class House:
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


h1 = House('ЖК Эльбрус', 12)
h2 = House('Домик в деревне', 3)
h1.go_to(5)
h2.go_to(12)
