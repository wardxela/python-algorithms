from random import choice

options = {
    'камень': 'ножницы',
    'ножницы': 'бумага',
    'бумага': 'камень'
}
print('Камень ножницы бумага\n')
while True:
    select = input('Ваш выбор: ').lower()
    if select not in options:
        print(
            f'''Варианта {select} не существует. Выберите {'/'.join(options)}''')
        continue
    else:
        bot_select = choice(list(options.keys()))
        print(f'Ваш выбор: {select}, Выбор робота: {bot_select}')
        if bot_select == select:
            print('Ничья')
        elif options[select] == bot_select:
            print('Вы выиграли!')
        else:
            print('Победил робот')
    play_again = input('Сыграть еще раз? [Да/Нет] ').lower()
    if play_again == 'да':
        continue
    else:
        break
