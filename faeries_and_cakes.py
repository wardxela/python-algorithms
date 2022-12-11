data = '''0.25
0.36
0.48
4
2'''

# Здесь я преобразую входные данные в список чисел
parsed_data = list(map(float, data.split('\n')))
# Деструктуризация списка - https://blog.teclado.com/destructuring-in-python/
*faeries_efficiency, minutes, cakes_count = parsed_data
# Здесь будем хранить подозреваемых фей
suspected_faeries = []
# По индексу будем определять старшинство феи
faeries = ['Младшая', 'Средняя', 'Старшая']
for i, faery_efficiency in enumerate(faeries_efficiency):
    if faery_efficiency * minutes >= cakes_count:
        suspected_faeries.append(f'{faeries[i]} феечка')
if len(suspected_faeries) == 0:
    print('Не они!')
else:
    print(' '.join(suspected_faeries))
