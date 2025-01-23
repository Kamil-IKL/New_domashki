class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    # метод для формирования атрибутов класса в строку
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'm07_dz-01_products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file: # такой синтаксис открытия файла позволяет
                                                                    # автоматически закрывать файл
            products = file.readlines()
        return ''.join(products)

    def add(self, *products):
        current_products = {} # создаю словарь продуктов

        # Считываю существующие продукты из файла и добавляю их в словарь
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                name, weight, category = line.strip().split(', ')
                current_products[(name, category)] = float(weight)

            for product in products:
                key = (product.name, product.category)
                if key in current_products:
                    # Увеличиваю вес существующего продукта
                    current_products[key] += product.weight
                    print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен"
                          f" {current_products[key]}")
                else:
                    # Добавляю новый продукт
                    current_products[key] = product.weight

        # Записываю обратно все продукты в файл
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for (name, category), weight in current_products.items():
                file.write(f'{name}, {weight}, {category}\n')


# проверка кода
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Бананы', 10.8, 'Фрукты')

s1.add(p1, p2, p3, p4)

print(s1.get_products())

