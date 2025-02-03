def add_everything_up(a: int, b: int):
    try:
        return round(a + b, 3)  # с учетом огруления
    except TypeError as exc:
        print(f'\nОдна из переменных тип - строка \n{exc}')
        a = str(a)
        b = str(b)
        return a + b # возвращаем конкатенацию строк


print(add_everything_up(123, 123))
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))