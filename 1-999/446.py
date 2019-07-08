# 446 Ровные делители
n = int(input())
tmp = 0
for i in range(1, n):
	if (n % i) == (int(n / i)):
		tmp += 1
print(tmp)
