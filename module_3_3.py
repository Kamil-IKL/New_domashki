def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 123, 'распаковка списка']
values_dict = {'a': 123, 'b': False, 'c': 'распаковка словаря'}


print_params(*values_list)
print_params(**values_dict)