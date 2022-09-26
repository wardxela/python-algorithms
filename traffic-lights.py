color = input().lower()

# if-else solution
if color == 'зеленый':
  print('Иди')
elif color == 'желтый':
  print('Скоро')
elif color == 'красный':
  print('Стой')
else:
  print('Такого цвета светофора не существует')

# match case solution
match color:
  case 'зеленый':
    print('Иди')
  case 'желтый':
    print('Скоро')
  case 'красный':
    print('Стой')
  case _:
    print('Такого цвета светофора не существует')

# dictionary solution
lights = {
  'зеленый': 'Иди',
  'желтый': 'Скоро',
  'красный': 'Стой'
}

if (color in lights):
  print(lights[color])
else:
  print('Такого цвета светофора не существует')