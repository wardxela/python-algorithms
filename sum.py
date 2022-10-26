# Программа основана на идее состояний
# Состояние 0 - начальное состояние
# Состояние 1 - состояние накопления суммы
# Состояние 2 - конец программы

acc = 0
state = 0
counter = 1

print('Доступные команды: start, end')
while True:
    if state == 0:
        command = input('Введите команду start ')
        if command == 'start':
            state = 1
        else:
            print('Неверный ввод. Я жду команду start')
    elif state == 1:
        numOrEnd = input(f'{counter}: ')
        if numOrEnd == 'end':
            state = 2
        else:
            try:
                num = int(numOrEnd)
                counter += 1
                acc += num
            except:
                print('Неверный ввод. Я жду число')
    elif state == 2:
        print(acc)
        break
