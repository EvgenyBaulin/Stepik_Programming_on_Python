import requests


def count_lines_in_file(url):
	response = requests.get(url.strip())

	if response.status_code != 200:
		print("Не удалось получить файл. Проверьте правильность URL.")
		return

	text = response.text
	lines = text.splitlines()
	line_count = len(lines)

	return line_count


with open("dataset_3378_2.txt", "r") as file:
	url = file.readline()

result = count_lines_in_file(url)

if result is not None:
	print("Число строк в файле:", result)
