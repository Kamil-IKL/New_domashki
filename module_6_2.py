# родительский класс - любой транспорт
class Vehicle:
    # варианты базовых цветов транспорта
    _COLOR_VARIANTS = ['Синий', 'Пурпурный', 'Зеленый', 'Черный', 'Белый']

    def __init__(self, owner: str, _model: str, _engine_power: int, _color: str):
        self.owner = str(owner)  # владелец транспорта
        self._model = str(_model)  # модель (марка) транспорта
        self._engine_power = int(_engine_power)  # мощность двигателя
        self._color = str(_color)  # название цвета

    def get_model(self):  # название модели транспорта
        return f'Модель: {self._model}'

    def get_horsepower(self):  # мощность двигателя транспорта
        return f'Мощность двигателя: {self._engine_power} л/c'

    def get_color(self):  # цвет транспорта
        return f'Цвет: {self._color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color: str):
        for color in self._COLOR_VARIANTS:
            if new_color.lower() in color.lower():
                self._color = new_color.upper()
                return None
        print(f'Нельзя сменить цвет на "{new_color.upper()}"')


# дочерний класс - транспорт "седан"
class Sedan(Vehicle):
    # # тоже рабочий вариант
    # def __init__(self, owner: str, _model: str, _engine_power: int, _color: str, _PASSENGERS_LIMIT=5):
    #     super().__init__(owner, _model, _engine_power, _color)
    #     self._PASSENGERS_LIMIT = _PASSENGERS_LIMIT

    _PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, _model: str, _engine_power: int, _color: str):
        super().__init__(owner, _model, _engine_power, _color)


# Текущие цвета _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Max', 'Toyota Mark II', 500, 'red')

print(f'\nИзначальные свойства'.upper())
vehicle1.print_info()
#
print(f'\nМеняем свойства (в т.ч. вызывая методы)'.upper())
vehicle1.set_color('красный')
vehicle1.set_color('бЕлыЙ')
vehicle1.owner = 'Vasyok'
#
print(f'\nПроверяем что поменялось'.upper())
vehicle1.print_info()
