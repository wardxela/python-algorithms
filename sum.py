from random import randint

acc = 0
shouldSum = False
current = randint(0, 10000)

print('Доступные команды: start, end')
while True:
    print(f'Текущее число: {current}')
    command = input('>>> ')

    if shouldSum:
        acc += current
        print('Текущая сумма:', acc)

    if command == 'start' and not shouldSum:
        print('Начинаю считать...')
        shouldSum = True
    elif command == 'end':
        break

    current += 1

print('Накопленная сумма:', acc)
