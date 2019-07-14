# 8952 152
n = int(input())
k = 1
tmp = True
for i in range(n):
	if k == n:
		tmp = False
	print(' ' * ((n -k)//2) + '*' * k + ' ' * ((n -k)//2))
	if tmp:
		k += 2
	else:
		k -= 2
