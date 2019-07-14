# 8957 157
n = int(input())
mass = [int(i) for i in input().split()]
s = []
for i in mass[::-1]:
	if i % 2 == 0:
		s.append(i)



if s:
	print(len(s))
	print(*s)
else:
	print('NO')
