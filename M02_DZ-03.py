my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):  # True
    if my_list[i] > 0:
        print('index', i, '=', my_list[i])
    i += 1
print(f'Проверены все {len(my_list)} элементов списка')
