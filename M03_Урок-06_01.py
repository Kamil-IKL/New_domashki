# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
salary = [2300, 1800.80, 5000, 1234.58, 7500.12]
print(len(salary))
print(sum(salary) / len(salary), ' - средняя зарплата компании')

print(max(salary), ' - максимальная зарплата компании')
print(min(salary), ' - минимальная зарплата компании')

salary_1 = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary_1) / len(salary_1), 2), ' - средняя зарплата компании')

print(round(max(salary_1), 2), ' - максимальная зарплата компании')
print(round(min(salary_1), 2), ' - минимальная зарплата компании')


names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = zip(names, salary_1)
# print(list(zipped))
print(dict(zipped))

zipped = dict(zip(names, salary_1))
print(zipped['Денис'], ' - зарплата Денис')