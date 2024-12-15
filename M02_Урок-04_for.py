# for i in 1, 20, 43, 4:
#     # print('ok')
#     print(i)

# for i in 'Kamil':
#     # print('ok')
#     print(i)

''' Работа со списками '''
# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
#     print(i)

# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)): # 0, 1, 2
#     sum_ += list_2[i]
#
# print(sum_)

'''таблица умножения'''
# for i in range(1, 11): # i - 1
#     for j in range(1, 11): # j - 1, 2, 3 ... 10
#         print(f'{i} x {j} = {i * j}')
#
# '''
# 1x1
# 1x2
# 1x3
#
# '''

''' Работа со словарями '''
dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict_)
# for i in dict_:
#     print(i, dict_[i])

for i, k in dict_.items():
    print(i, k)