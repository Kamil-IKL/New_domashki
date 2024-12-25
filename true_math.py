from math import inf

def divide(first: int, second: int):
    first = int(first)
    second = int(second)
    if second == 0:
        return f'{inf}: Положительная бесконечность'
    return first / second


# print(divide(2, 0))