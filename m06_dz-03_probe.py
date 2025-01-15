# класс описывающий животных
import random


class Animal:
    live = True

    # звук (изначально отсутствует)
    sound = None

    # степень опасности существа
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed  # скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):
        self.dx = int(dx)
        self.dy = int(dy)
        self.dz = int(dz)
        # self._cords = self.speed*[dx,dy,dz]

    def get_cords(self):
        print(f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        _DEGREE_OF_DANGER = self._DEGREE_OF_DANGER
        if self._DEGREE_OF_DANGER < 5:
            print(f"Извините, я мирный :)")
            return
        elif self._DEGREE_OF_DANGER >= 5:
            # print(f"'Be careful, i'm attacking you 0_0'")
            print(f'Будь осторожен, я нападаю на тебя 0_0')
            return


# класс описывающий птиц
class Bird:
    beak = True

    def lay_eggs():
        # print(f'"Here are(is) {random.randint(1, 4)} eggs for you"')
        print(f'Вот (есть) {random.randint(1, 4)} яиц для тебя')
        return


# класс описывающий плавающего животного
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    pass

# класс описывающий ядовитых животных
class PoisonousAnimal:
    _DEGREE_OF_DANGER = 8
    pass


# класс описывающий утконоса
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    pass


    # звук, который издаёт утконос
    sound = "Click-click-click"
    pass



if __name__ == '__main__':
    print('проверка'.upper())
    a1 = Animal
    print(a1.live)
    print(a1.sound)
    print(a1._DEGREE_OF_DANGER)
    # print(a1.move( 0,1, 2, 1))
    a1.attack()


    b1 = Bird
    b1.lay_eggs()
