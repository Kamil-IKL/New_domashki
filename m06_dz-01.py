class Animal:  # класс Животные
    alive = True  # живой
    fed = False  # True - накормленный, False - не накормленный

    def __init__(self, name):
        self.name = name


class Plant:  # класс Растение
    edible = False  # съедобный

    def __init__(self, name):
        self.name = name


class Mammal(Animal):  # класс Млекопитающее
    def eat(self, food):
        self.food = food # пища
        if self.food is Plant.edible:
            print(f"{self.name} съел {food.name}")
            return Animal.fed == True
        else:
            print(f'{self.name} не стал есть {food.name}')
            return Animal.fed == False


class Predator(Animal):  # класс Хищник
    def eat(self, food):
        self.food = food
        if self.food is Plant.edible:
            print(f"{self.name} съел {food.name}")


class Flower(Plant):
    # if Plant.edible is False:
    pass



class Fruit(Plant):
    pass


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
