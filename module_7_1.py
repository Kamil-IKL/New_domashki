class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    # ����� ��� ������������ ��������� ������ � ������
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'm07_dz-01_products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file: # ����� ��������� �������� ����� ���������
                                                                    # ������������� ��������� ����
            products = file.readlines()
        return ''.join(products)

    def add(self, *products):
        current_products = {} # ������ ������� ���������

        # �������� ������������ �������� �� ����� � �������� �� � �������
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                name, weight, category = line.strip().split(', ')
                current_products[(name, category)] = float(weight)

            for product in products:
                key = (product.name, product.category)
                if key in current_products:
                    # ���������� ��� ������������� ��������
                    current_products[key] += product.weight
                    print(f"������� {product.name} ��� ��� � ��������, ��� ����� ��� ������ �����"
                          f" {current_products[key]}")
                else:
                    # �������� ����� �������
                    current_products[key] = product.weight

        # ��������� ������� ��� �������� � ����
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for (name, category), weight in current_products.items():
                file.write(f'{name}, {weight}, {category}\n')


# �������� ����
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('������', 10.8, '������')

s1.add(p1, p2, p3, p4)

print(s1.get_products())

