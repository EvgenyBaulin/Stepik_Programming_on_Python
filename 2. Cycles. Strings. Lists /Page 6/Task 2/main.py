a = int(input())
m = []
for i in range(a):
	j = 0
	while j < i + 1:
		m.append(i + 1)
		j += 1
	if len(m) > a: break
m = m[0:a]
for i in m:
	print(i, end = " ")
