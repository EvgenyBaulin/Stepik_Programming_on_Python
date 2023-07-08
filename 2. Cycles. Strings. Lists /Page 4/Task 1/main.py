s = input().upper()
a = s.count('C') + s.count('G')
print(float(a / len(s)) * 100)
