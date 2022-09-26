# Примечание: данный код работает только на Windows (я использую msvcrt для чтения символов из терминала)
# class Dye - инкапсулирует работу с цветом текста в терминале (работает с помощью ANSI-последовательностей)
# class Terminal - ядро всего приложения. Обеспечивает вывод/ввод состояния игры
# def beautiful_print() - реализует 'плавный', 'анимированный' вывод в консоль

# И последнее, я совсем не гуманитарий, извините за краткость сюжета. :)

from ast import List
import msvcrt
from time import sleep
import sys
import os


class Dye:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'

    def colorize(color: str, text: str):
        return f'{color}{text}\033[0m'

    def red(text: str):
        return Dye.colorize(Dye.RED, text)

    def green(text: str):
        return Dye.colorize(Dye.GREEN, text)

    def yellow(text: str):
        return Dye.colorize(Dye.YELLOW, text)

    def blue(text: str):
        return Dye.colorize(Dye.BLUE, text)

    def magenta(text: str):
        return Dye.colorize(Dye.MAGENTA, text)

    def cyan(text: str):
        return Dye.colorize(Dye.CYAN, text)


class Terminal:
    def __init__(self, introduction=''):
        self.state = introduction
        self.update()

    def write(self, text: str, isSlow=True, wrap=True):
        if len(text) == 0:
            return
        if wrap:
            text = text + '\n'
        self.state += text
        beautiful_print(text) if isSlow else print(text, end="")

    def update(self):
        Terminal.clear()
        print(self.state, end="")

    def clear():
        os.system('cls')

    def wait(self):
        byte = None
        while byte != b'\r':
            print('Нажмите Enter, чтобы продолжить')
            byte = msvcrt.getch()
            self.update()

    def choose(self, options: List, question='') -> str:
        self.write(question)
        byte = None
        choice = 0
        should_render = True
        while byte != b'\r':
            if should_render:
                if byte == b'H':
                    choice = len(options) - 1 if choice == 0 else choice - 1
                elif byte == b'P':
                    choice = (choice + 1) % len(options)

                self.update()
                print(options_to_str(options, choice, Dye.YELLOW), end="")
                should_render = False
            byte = msvcrt.getch()
            if byte == b'\xe0' or byte == b'\x00':
                should_render = True
                byte = msvcrt.getch()
        self.update()
        self.write(options_to_str(options, choice, Dye.GREEN),
                   isSlow=False, wrap=False)
        return options[choice]

    def ask(self, question: str):
        self.write(question, wrap=False)
        value = ''
        while len(value) == 0:
            value = input()
        self.update()
        self.write(Dye.green(value), isSlow=False)
        return value


def beautiful_print(text: str):
    for letter in text:
        sleep(0.02)
        print(letter, end="")
        sys.stdout.flush()


def options_to_str(options: List, active: int, color: str):
    result = ''
    for i, option in enumerate(options):
        if i == active:
            result += Dye.colorize(color, f'[x] {option}\n')
        else:
            result += f'[ ] {option}\n'
    return result


terminal = Terminal()
terminal.write(f'''{Dye.cyan('Человек упавший с луны')}
19.09.6045 23:55
Марс. Близ Земля Ноя. Секретная лаборатория Л320.''')
terminal.write('Приветствую вас, наконец-то вы пришли в себя.')
user = terminal.ask('Назовитесь, пожалуйста: ')
terminal.write(f'Я рад нашему знакомству, {Dye.green(user)}')
question = terminal.choose(['Кто ты?', 'Что происходит?'])
if question == 'Кто ты?':
    terminal.write(
        f'''Я искусственный интеллект, служащий человеку. Мое имя - {Dye.cyan('RA9')}.''')
else:
    terminal.write(
        'Роботы-специалисты восстанавливают ваши человеческие способности.')

terminal.choose(['Я ничего не помню', 'Где люди?'])
terminal.write(f'''Много лет назад мир был населён всеми видами живой материи и находился в состоянии благополучия и процветания, нам даже удалось прожить несколько столетий без голода и войн.
Но глобальная катастрофа, обрушившаяся на нас вследствие бездумной человеческой деятельности оставила от планеты только ее гордое название, в связи с чем мы были вынуждены колонизировать {Dye.red('Марс')}.''')
terminal.choose(['Как такое может быть?', 'Я в это не верю'])
terminal.write(
    f'''Человеческое существование на грани вымирания. Вероятнее всего вы один из последних людей, оставшихся в живых.
Ваше тело найдено в близи Кратера Дельта. Скорее всего вас доставил кто-то извне. Наши специалисты считают, что вы упали с {Dye.cyan('луны')}''')
terminal.choose(['Что будет дальше?', 'Что мне делать?'])
terminal.write(f'''Вам следует отдохнуть. Ваше здоровье по прежнему оставляет желать лучшего.
Мой заряд на исходе, я вынужден отправиться в соседний корпус. Оставайтесь на месте.
{Dye.cyan('RA9 покидает комнату')}''')
terminal.wait()
terminal.write(Dye.yellow(
    'Боюсь не подобрать слов к тому что не описать словами. Марс? Роботы? Вымирание? Ощущение, будто я проспал несколько тысяч лет. В это просто невозможно поверить'))
terminal.wait()
terminal.write(
    Dye.yellow(
        'Кажется, этот робот оставил дверь открытой, стоит ли мне попытаться сбежать?')
)
question = terminal.choose(
    ['Сбежать', 'Остаться на месте'], 'Как вы поступите?')
if question == 'Сбежать':
    terminal.write(Dye.yellow(
        f'''Действительно, зачем мне его слушать? Нужно как можно скорее выбираться отсюда и выяснить, что же на самом деле здесь происходит.'''))
    terminal.wait()
    terminal.write(Dye.blue('Вы покидаете лабораторию'))
    terminal.wait()
    terminal.write(Dye.magenta('СТОЯТЬ! Кто вы такой и куда бежите?'))
    question = terminal.choose(
        [f'Мое имя {user}. Я потерялся.', 'Не ваше дело'])
    if question == 'Не ваше дело':
        terminal.write(Dye.magenta(
            'Как грубо с вашей стороны. Я всего лишь хотела помочь. А за такое отношение ко мне вам грозит штраф. Немедленно извинитесь'))
        terminal.choose(['Извините'])
        terminal.write(Dye.magenta(
            'Вот так то лучше. А теперь ответьте мне четко, куда вы бежите?'))
    else:
        terminal.write(Dye.magenta('Скажите, куда вы так усердно торопитесь?'))
    terminal.choose(
        ['Я бегу из лаборатории Л320, кажется, у меня амнезия'])
    terminal.write(Dye.magenta(
        f'Точно, вы же {user}. Отправляйтесь за мной.'))
    terminal.wait()
    terminal.write(
        Dye.blue('Вы оказались у соседнего корпуса с лабораторией Л320'))
    terminal.wait()
    terminal.write(
        f'''{Dye.red(user + '!?')} Что ты здесь делаешь? Я просил тебя оставаться на месте''')
    terminal.choose(['Я испугался', 'Промолчать'])
    terminal.write(
        'Больше никогда так не делайте. Вы очень дорогой для нас человек.')
else:
    terminal.write(Dye.yellow(
        f'''Пока что я мало осознаю происходящее, но этот робот был заботлив ко мне. Останусь здесь.'''))
    terminal.wait()
    terminal.write(Dye.blue('Проходит несколько минут. Робот возвращается.'))
    terminal.wait()
    terminal.write(
        'Спасибо за ваше терпение, теперь моей батареи хватит на несколько дней.')
terminal.wait()
terminal.write('Только что поступила новость, что неподалеку от нашей лаборатории образовался новый кратер. Нам нужна ваша помощь. Вы согласны отправиться туда прямо сейчас?')
question = terminal.choose(['Да', 'Нет'])
if question == 'Нет':
    terminal.write('Я понимаю ваше тяжелое положение, вы еще не пришли в себя. Но вы не представляете важность происходящего. От текущего события зависит продолжение жизни на этой планете')
    terminal.write(Dye.yellow(
        'Видимо у меня не остается другого выбора. Я согласен.'))
terminal.write(
    'В таком случае поторопимся. Корабль ждет нас прямо у выхода.')
terminal.wait()
terminal.write(Dye.blue('Вы оказываетесь вблизи кратера Арго.'))
terminal.wait()
terminal.choose(['Да', 'Конечно'],
                'Мы на месте. Вы готовы рассмотреть объект ближе?')
terminal.write('Отлично, вперед.')
terminal.wait()
terminal.write(
    f'''Перед нами космический корабль {Dye.cyan('"Куб Боргов"')}. Такие были в обиходе еще 500 лет назад.''')
terminal.choose(['Что это значит?', 'Как такое возможно?'])
terminal.write('Кажется это уже начинается...')
terminal.wait()
terminal.write(f'{user}, мы выбрали тебя неслучайно. Нет времени все объяснять. Ты - последняя надежда на наше спасение. Твоя задача - вернуться на Землю и возродить на ней жизнь. В корабле есть все необходимое, чтобы это сделать: почва, образцы растений и многое другое.')
question = terminal.choose(
    ['Да', 'Нет'], 'Согласны ли вы отравиться на Землю, чтобы спасти человечество?')
if question == 'Да':
    terminal.write('Спасибо за понимание. Корабль уже ждёт вас')
    terminal.wait()
    terminal.write(Dye.blue(
        'Добравшись до Земли вы видите всю правду своими глазами: разрушенные города, сгоревшие леса, высохшие водоёмы - все это уже не кажется вам бредом сумасшедшего.'))
    terminal.wait()
    terminal.write(Dye.blue(
        'Остановившись вблизи экватора, вы приступаете к делу: размещаете растения по периметру, возрождаете источники воды - одним словом, начинаете новую жизнь.'))
    terminal.wait()
    terminal.write(Dye.blue('Спустя 100 лет. Земля. Отрывок из новостей.'))
    terminal.write(Dye.magenta(
        f'"Сегодня по настоящему важный и знаковый для нас день. Ровно век назад, герой по имени {user} восстановил жизнь на этой планете. Отблагодарим его смелость, отвагу и упорство минутой молчания"'))
    terminal.write(Dye.green('Достижение: хороший финал'))
    terminal.write('[싸이 "강남스타일" 가사]')

else:
    terminal.write('Ты не можешь так поступить. На кону стоят все жизни')
    terminal.choose(['Мне все равно', 'Я тебе не доверяю'])
    terminal.write('Ты не оставляешь мне выбора...')
    terminal.wait()
    terminal.write(Dye.yellow('Что ты творишь!?'))
    terminal.wait()
    terminal.write('Я вынужден ликвидировать вас.')
    terminal.wait()
    terminal.write(Dye.red('Вы погибаете от радиации'))
    terminal.write(Dye.red('Достижение: печальный конец'))
