def generate_spiral_table(n):
	table_nums = [[0] * n for _ in range(n)]

	top = 0
	bottom = n - 1
	left = 0
	right = n - 1

	num = 1
	direction = 0

	while top <= bottom and left <= right:
		if direction == 0:
			for i in range(left, right + 1):
				table_nums[top][i] = num
				num += 1
			top += 1
			direction = 1
		elif direction == 1:
			for i in range(top, bottom + 1):
				table_nums[i][right] = num
				num += 1
			right -= 1
			direction = 2
		elif direction == 2:
			for i in range(right, left - 1, -1):
				table_nums[bottom][i] = num
				num += 1
			bottom -= 1
			direction = 3
		elif direction == 3:
			for i in range(bottom, top - 1, -1):
				table_nums[i][left] = num
				num += 1
			left += 1
			direction = 0

	return table_nums


n = int(input())
table = generate_spiral_table(n)

for row in table:
	print(' '.join(str(num) for num in row))
