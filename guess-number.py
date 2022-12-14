from random import randint

print('Угадай число от 1 до 1000\n')
num_to_guess = randint(1, 1000)
total_attempts = left_attempts = 10
won = False
while left_attempts > 0:
    left_attempts -= 1
    attempt = int(input('Ваше ответ: '))
    if num_to_guess == attempt:
        won = True
        break
    if num_to_guess * 0.9 < attempt and num_to_guess * 1.1 > attempt:
        print('Горячо')
    elif num_to_guess * 0.7 < attempt and num_to_guess * 1.3 > attempt:
        print('Теплее')
    else:
        print('Холодно')
    print('Попробуй число ', end='')
    print('побольше' if num_to_guess > attempt else 'поменьше')
    print(f'Осталось попыток: {left_attempts}\n')
if won:
    print(
        f'Число угадано за {total_attempts - left_attempts} попыток. Поздравляю!')
else:
    print('К сожалению, вам не повезло в этот раз')
    print(f'Правильный ответ - {num_to_guess}')
