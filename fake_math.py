def divide(first: int, second: int):
    first = int(first)
    second = int(second)
    if second == 0:
        return 'Error: '.upper() + 'Делить на 0 нельзя !!!'
    return first / second


# print(divide(2, 0))