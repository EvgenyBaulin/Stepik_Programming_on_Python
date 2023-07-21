n = int(input())

point = [0, 0]

for _ in range(n):
	move = input().split(' ')

	if move[0] == "север":
		point[1] += int(move[1])
	elif move[0] == "юг":
		point[1] -= int(move[1])
	elif move[0] == "восток":
		point[0] += int(move[1])
	else:
		point[0] -= int(move[1])

print(f'{point[0]} {point[1]}')
