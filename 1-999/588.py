# 588 Игра
n = int(input())
mass = [int(i) for i in input().split()]
p = 0
if n > 1:
	d = abs(mass[1] - mass[0])
	for i in range(2,n):
		if abs(mass[i-1] - mass[i]) + d < 3 * abs(mass[i-2] - mass[i]) + p:
			p = d
			d += abs(mass[i-1] - mass[i])
		else:
			t = d
			d = 3 * abs(mass[i-2] - mass[i]) + p
			p = t
print(d)
