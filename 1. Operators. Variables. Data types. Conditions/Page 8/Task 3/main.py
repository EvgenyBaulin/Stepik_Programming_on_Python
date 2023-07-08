X = int(input())
H = int(input())
M = int(input())

if X % 60 + M < 60:
	print(X // 60 + H)
	print(X % 60 + M)
else:
	print(X // 60 + H + 1)
	print(X % 60 + M - 60)
