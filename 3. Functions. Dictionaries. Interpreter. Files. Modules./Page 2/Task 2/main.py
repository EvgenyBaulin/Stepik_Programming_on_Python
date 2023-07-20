input_new = input().split(' ')

for i in range(len(input_new)):
	input_new[i] = input_new[i].lower()

words = {}

for i in input_new:
	# noinspection PyTypeChecker
	words[i] = input_new.count(i)

for key, value in words.items():
	print(key, value)
