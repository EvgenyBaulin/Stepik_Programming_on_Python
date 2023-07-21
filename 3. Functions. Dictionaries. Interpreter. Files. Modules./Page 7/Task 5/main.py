def read_file(file_path):
	data = {}
	counts = {}

	with open(file_path, 'r') as file:
		for line in file:
			class_num, name, height = line.strip().split('\t')
			class_num = int(class_num)
			height = int(height)

			# Суммируем рост для каждого класса
			data[class_num] = data.get(class_num, 0) + height

			# Увеличиваем количество учеников в каждом классе
			counts[class_num] = counts.get(class_num, 0) + 1

	return data, counts


def calculate_averages(data, counts):
	averages = {}
	for class_num in range(1, 12):
		# Если информации о классе нет, ставим прочерк
		if class_num not in data or class_num not in counts:
			averages[class_num] = "-"
		else:
			# Вычисляем средний рост для класса
			average_height = data[class_num] / counts[class_num]
			averages[class_num] = average_height

	return averages


def write_output(file_path, averages):
	with open(file_path, 'w') as file:
		for class_num, average_height in averages.items():
			file.write(f"{class_num} {average_height}\n")


input_file_path = "dataset_3380_5.txt"
output_file_path = "output.txt"

data, counts = read_file(input_file_path)
averages = calculate_averages(data, counts)
write_output(output_file_path, averages)
