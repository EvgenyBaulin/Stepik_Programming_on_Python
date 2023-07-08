a = [int(i) for i in input().split()]
if len(a) == 1:
	print(a[0])
else:
	for j in range(len(a) - 1):
		print(a[j - 1] + a[j + 1], end = ' ')
	print(a[len(a) - 2] + a[0])
