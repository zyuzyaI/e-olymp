# 5846 Компьютерная игра (платформы)
def f(n, mass):
	e = [0]*(n)

	e[1] = abs(mass[0]-mass[1])

	for i in range(2, n):
		a = e[i - 1] + abs(mass[i-1]-mass[i])
		b = e[i - 2] + 3 * abs(mass[i] - mass[i - 2])
		if a < b :
			e[i] = a

		else:
			e[i] = b


	print(e[-1])




n = int(input())
mass = [int(i) for i in input().split()]

f(n,mass)
