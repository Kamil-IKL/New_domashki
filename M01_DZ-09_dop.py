grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

''' преоброзовываю множество в список '''
new_students = list(students)
# print(new_students, type(new_students))

''' сортирую его по алфавиту '''
new_students = sorted(new_students)
# print(new_students, type(new_students))

''' создаю новый список со средним баллом студента
("sum"-суммирую оценки каждого студента, "len"- количество оценок по каждому студенту, "round"- округляю до сотых) '''
new_grades = [round(sum(grades[0])/len(grades[0]),2), round(sum(grades[1])/len(grades[1]),2),
              round(sum(grades[2])/len(grades[2]),2), round(sum(grades[3])/len(grades[3]),2),
              round(sum(grades[4])/len(grades[4]),2)]
# print(new_grades, type(new_grades))

''' объединяю два списка в новый словарь студентов '''
new_dict = dict(zip(new_students, new_grades))
print(new_dict)






