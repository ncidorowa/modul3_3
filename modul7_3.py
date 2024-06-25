

# Использование %:
team1_num = 4
team2_num = 6
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

print('В команде Мастера кода участников: %d! ' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Использование format():
score_1 = 26
score_2 = 36
team1_time = 12473
team2_time = 13060
print('Команда "Волшебники данных" решила задач: {}!'.format(score_1))
print('Команда "Мастера кода" решила задач: {}!'.format(score_2))
print('"Волшебники данных" решили задачи за {} с!'.format(team1_time))
print('"Мастера кода" решили задачи за {} с!'.format(team2_time))


# Использование f-строк:

challenge_result = 'Кто то должен победить!!!'
tasks_total = 62
time_avg = 411

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')



if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')






