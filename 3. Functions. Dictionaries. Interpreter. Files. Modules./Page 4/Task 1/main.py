with open('dataset_3363_2.txt', 'r') as f:
	string = f.read().strip()
string_new = ''

char = string[0]
i = 1
while i < len(string):
	if string[i].isdigit():
		count = ''
		while i < len(string) and string[i].isdigit():
			count += string[i]
			i += 1
	else:
		string_new += char * int(count)
		char = string[i]
		i += 1

string_new += char * int(count)

print(string_new)
