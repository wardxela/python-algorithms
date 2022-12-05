import re

alphabet_map = {
    'а': '4',
    'е': '3',
    'и': '1',
    'о': '0',
    'с': '5'
}


def hacker_speak(text):
    return re.sub(r'[аеиос]', lambda m: alphabet_map[m.group(0)], text)


print(hacker_speak('джаваскрипт крутой'))
print(hacker_speak('программирование это весело'))
print(hacker_speak('стань программистом'))
