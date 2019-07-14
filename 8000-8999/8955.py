# 8955 155
n  = int(input())
mass =[int(i) for i in  input().split()]
tmp = []
for i in mass:
	if i > 0:
		tmp.append(i)
if tmp:
	print(len(tmp))
	print(*tmp)
else:
	print('NO')
