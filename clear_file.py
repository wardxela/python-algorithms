import re

src = 'data/to_be_cleared.txt'

words_to_exclude = input('Перечислите слова для удаления: ').split()
placeholder = input('Введите слово-замену: ')
regexp_words_to_exclude = rf'{"|".join(words_to_exclude)}'

with open(src, encoding='utf-8') as file:
    content = file.read()
    count = len(re.findall(regexp_words_to_exclude, content, flags=re.I))
    content = re.sub(regexp_words_to_exclude, placeholder, content, flags=re.I)

with open(src, 'w', encoding='utf-8') as file:
    file.write(content)

print(f'Найдено совпадений: {count}')
