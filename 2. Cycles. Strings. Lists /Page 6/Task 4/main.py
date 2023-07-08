mass = []
new_mass = []

while True:
	a = input()
	if a == "end":
		break
	else:
		add_mass = [int(i) for i in a.split()]
		mass.append(add_mass)

for i in range(len(mass)):

	add_new_mass = []
	for j in range(len(mass[i])):

		if i == 0:
			element_1 = mass[len(mass) - 1][j]
		else:
			element_1 = mass[i - 1][j]

		if j == 0:
			element_2 = mass[i][len(mass[i]) - 1]
		else:
			element_2 = mass[i][j - 1]

		if i == len(mass) - 1:
			element_3 = mass[0][j]
		else:
			element_3 = mass[i + 1][j]

		if j == len(mass[i]) - 1:
			element_4 = mass[i][0]
		else:
			element_4 = mass[i][j + 1]

		add_mass_element = element_1 + element_2 + element_3 + element_4
		add_new_mass.append(add_mass_element)
	new_mass.append(add_new_mass)

for i in range(len(new_mass)):
	for j in range(len(new_mass[i])):
		print(new_mass[i][j], end = ' ')
	print()
