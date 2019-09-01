#6955 Максимальный объем
n = int(input())

p = 3.14159
'''cone = 1/3 * p * r * r * h
cylinder = p * r * r * h
sphere = 4/3 * p * r * r * r '''
tmp = 0
counter = 0
for i in range(n):
	k = input().split()
	if k[0] == 'S':
		r = float(k[1])
		counter = 4/3 * p * r * r * r
	elif k[0] == 'C':
		r, h = float(k[1]), float(k[2])
		counter = 1/3 * p * r * r * h
	elif k[0] == 'L':
		r, h = float(k[1]), float(k[2])
		counter = p * r * r * h
	if tmp < counter:
		tmp = counter

print('{:.3f}'.format(tmp))
