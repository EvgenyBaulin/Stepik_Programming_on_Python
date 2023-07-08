a = int(input())
b = a // 1000
c = a % 1000

suma1 = 0
suma2 = 0

while b > 0:
	digit = b % 10
	suma1 = suma1 + digit
	b = b // 10

while c > 0:
	digit = c % 10
	suma2 = suma2 + digit
	c = c // 10

if suma1 == suma2:
	print('Счастливый')
else:
	print('Обычный')
