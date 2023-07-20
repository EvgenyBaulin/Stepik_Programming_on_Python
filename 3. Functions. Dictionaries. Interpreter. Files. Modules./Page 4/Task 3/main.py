input_file_name = 'dataset_3363_4.txt'
output_file_name = 'output_file.txt'

open(output_file_name, 'w')

with open(input_file_name, 'r') as file:
	lines = [line.strip() for line in file]

PHI = 0
MATH = 0
RUS = 0

for i in lines:
	i = i.split(";")
	math = int(i[1])
	phi = int(i[2])
	rus = int(i[3])
	# noinspection PyTypeChecker
	average = (math + phi + rus) / 3
	MATH += math
	PHI += phi
	RUS += rus
	with open(output_file_name, 'a') as file:
		file.write(str(average) + '\n')

with open(output_file_name, 'a') as file:
	file.write(str(MATH / len(lines)) + ' ' + str(PHI / len(lines)) + ' ' + str(RUS / len(lines)))
