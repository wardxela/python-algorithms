import re


with open('./data/reactions.txt', encoding="utf-8") as f:
    content = f.read()
    positive_count = len(re.findall(r'хорош|добр', content))
    negative_count = len(re.findall(r'зло|плох', content))
    additional_characteristic = 'В КРАПИНКУ' if 'очень' in content else 'ОДНОТОННЫЙ'
    if positive_count >= negative_count:
        print('СВЕТЛЫЙ')
    else:
        print('ТЕМНЫЙ')
    print(additional_characteristic)
