a = float(input())
b = float(input())
c = str(input())

if (c == 'div' or c == '/' or c == 'mod') and b == 0:
	print('Деление на 0!')
elif c == '+':
	print(a + b)
elif c == '-':
	print(a - b)
elif c == '/':
	print(a / b)
elif c == '*':
	print(a * b)
elif c == 'mod':
	print(a % b)
elif c == 'pow':
	print(a ** b)
else:
	print(a // b)
