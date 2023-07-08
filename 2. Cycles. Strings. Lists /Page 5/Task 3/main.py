a = [int(i) for i in input().split()]
b = {x for x in a if a.count(x) > 1}
print(*b)
