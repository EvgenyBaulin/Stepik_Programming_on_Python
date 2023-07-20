def modify_list(l):
	i = 0
	while i < len(l):
		if l[i] % 2 == 1:
			del l[i]
		else:
			l[i] = l[i] // 2
			i += 1


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]
