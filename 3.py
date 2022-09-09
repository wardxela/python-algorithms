a = int(input('1 сторона: '))
b = int(input('2 сторона: '))
c = int(input('3 сторона: '))

if (a + b > c and a + c > b and b + c > a):
  print('Существует')
else:
  print('Не существует')