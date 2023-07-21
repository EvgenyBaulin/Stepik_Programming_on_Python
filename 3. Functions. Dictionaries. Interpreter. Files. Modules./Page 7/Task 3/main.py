d = int(input())
correct = []

for _ in range(d):
	correct.append(input().lower())

l = int(input())
text = []

for _ in range(l):
	for i in input().lower().split(' '):
		text.append(i)

uncorrect = []

for i in text:
	if i in correct:
		continue
	if i in uncorrect:
		continue
	uncorrect.append(i)
	print(i)
