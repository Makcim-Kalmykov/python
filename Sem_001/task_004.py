# Программа загадывает число от 0 до 1000. Неоюходимо угадать за 10 попыток. Программа должна подсказать больше или меньше после каждой попытки.

from random import randint
MIN_NUM = 0
MAX_NUM  = 1000
NUM_ATTEMPTS = 10

num = randint(MIN_NUM, MAX_NUM)
for i in range(1, NUM_ATTEMPTS):
    num_input = int(input('Угадайте число от 0 до 1000 '))
    if num_input == num:
        print('Вы угадали')
    elif num_input > num:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
    print(f'Осталось {NUM_ATTEMPTS - i} попыток')
    i += 1