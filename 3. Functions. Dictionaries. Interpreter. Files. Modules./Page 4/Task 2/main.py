with open('dataset_3363_3.txt', 'r') as file:
	input_new = [word.lower() for line in file for word in line.strip().split()]

words = {}

for i in input_new:
	# noinspection PyTypeChecker
	words[i] = input_new.count(i)

max_key, max_value = [], 0

# noinspection PyTypeChecker
for key, value in words.items():
	if max_value == value:
		max_key.append(key)
	elif max_value < value:
		max_key = [key]
		max_value = value

max_key.sort()

for i in max_key:
	print(i, max_value)
