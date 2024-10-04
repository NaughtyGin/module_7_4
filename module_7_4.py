sym = '!'
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / (score_2 + score_1), 1)
challenge_result = None
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = f'победа команды {team1}{sym}'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = f'победа команды {team2}{sym}'
else:
    challenge_result = f'Ничья!'

print('Использование %:')
print('В команде %(team)s участников: %(num)s%(sym)s' % {'team': team1, 'num': team1_num, 'sym': sym})
print('Итого сегодня в командах участников: %s и %s%s' % (team1_num, team2_num, sym))
print()
print('Использование format():')
print('Команда {} решила задач: {}{}'.format(team2, score_2, sym))
print('{} решили задачи за {} с{}'.format(team2, team2_time, sym))
print()
print('Использование f-строк:')
print(f'Команды решили {score_1} и {score_2} задач(и).')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач(и), в среднем по {time_avg} секунд(ы) на задачу!')
