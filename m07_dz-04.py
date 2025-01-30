# Использование %
team1 = '"Мастера кода"'
team2 = '"Волшебники"'
print('Играют команды: %s и %s' % (team1, team2))

team1_num = 5  # кол-во участников команды "Мастера кода"
print('В команде Мастера кода участников: %s!' % team1_num)

team2_num = 6  # кол-во участников команды "Волшебники"
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование format()
score_2 = 42  # количество задач решённых командой "Волшебники"
print('Команда Волшебники данных решила задач: {}!'.format(score_2))

team1_time = 1552.512
print('Волшебники данных решили задачи за {}с !'.format(team1_time))

team2_time = 2153.31451

# Использование f-строк:
score_1 = 40  # количество задач решённых командой "Мастера кода"
print(f'Команды решили {score_1} и {score_2} задач.')

tasks_total = score_1 + score_2
print(
    f'Сегодня было решено {tasks_total} задач, в среднем по {round((team1_time + team2_time) / tasks_total, 1)} секунды на задачу!')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = print(f'Победа команды {team1}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = print(f'Победа команды {team2} Данных!')
else:
    challenge_result = 'Ничья!'
