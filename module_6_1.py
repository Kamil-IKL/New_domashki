class Animal:   # родительский класс Животные
    def __init__(self, name):
        self.name = name    # индивидуальное название животного
        self.alive = True   # True - живое, False - неживое
        self.fed = False    # True - накормленный, False - ненакормленный


class Plant:    # родительский класс Растение
    def __init__(self, name):
        self.name = name    # индивидуальное название растения
        self.edible = False # True - съедобный, False - несъедобный


class Mammal(Animal):   # дочерний класс Млекопитающее
    def eat(self, food):    # food - это пища
        self.food = food    # пища
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal): # дочерний класс Хищник
    def eat(self, food):    # метод "есть"
        self.food = food    # пища
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):    # дочерний класс Цветы -  не съедобный
    pass


class Fruit(Plant): # дочерний класс Фрукты
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(f'\nПроверка переданного параметра "name" в род. и доч. классы'.upper())
print(f'{a1.name} - для объекта род.класса "Predator - Хищник"')
print(f'{p1.name} - для объекта доч.класса "Flower(Plant) - Цветок(Растение)"')

print(f'\nПроверка пространств имен, втч видимость атрибутов род. класса из доч.класса'.upper())
print(f'{a1.alive} - атрибут "alive(живой)" из род.класса "Predator -Хищник"')
print(f'{a2.fed} - атрибут "fed(накормленный)" из род.класса "Predator -Хищник"')

print(f'\nПроверка метода "есть"'.upper())
a1.eat(p1)
a2.eat(p2)

print(f'\nПроверка атрибутов "на выходе"'.upper())
print(f'{a1.alive} - атрибут "живой" для экземпляра "{a1.name}" объекта "Animal"')
print(f'{a2.fed} - атрибут "накормленный" для объекта "{a2.name}" объекта "Animal"')

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
