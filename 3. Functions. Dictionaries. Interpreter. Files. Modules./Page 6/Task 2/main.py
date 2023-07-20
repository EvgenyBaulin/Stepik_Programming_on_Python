import requests


def text_file(name):
	response = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + name).text
	if not response.startswith("We"):
		text_file(response)
	else:
		print(response)
		return


text_file('699991.txt')
