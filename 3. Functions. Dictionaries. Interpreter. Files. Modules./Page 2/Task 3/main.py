n = int(input())
repeat = {}

for _ in range(n):
	num = int(input())
	if num in repeat:
		result = repeat[num]
	else:
		result = f(num)
		repeat[num] = result
	print(result)
