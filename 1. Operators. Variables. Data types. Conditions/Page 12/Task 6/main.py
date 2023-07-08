n = int(input())
if n % 10 == 1 and n % 100 != 11:
	print(n, 'программист')
elif 10 < n % 100 < 15:
	print(n, 'программистов')
elif 1 < n % 10 < 5:
	print(n, 'программиста')
else:
	print(n, 'программистов')
