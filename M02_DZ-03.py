my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
'''Замечания;
   По заданию при встрече с отрицательным числом следует прервать цикл'''
# i = 0
# while i < len(my_list):  # True
#     if my_list[i] > 0:
#         print('index', i, '=', my_list[i])
#     i += 1
# print(f'Проверены все {len(my_list)} элементов списка')

'''с учетом замечания при проверке'''
i = 0
while i < len(my_list) and my_list[i] >= 0:
    print('index', i, '=', my_list[i])
    i += 1
