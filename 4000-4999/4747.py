# 4747 Разложение на простые множители - 2
def factor(n):
	ans = []
	d = 2
	while d*d <= n:
		if n % d == 0:
			ans.append(d)
			n //= d
		else:
			d += 1
	if n > 1:
		ans.append(n)
	return ans

n = int(input())
ans = []
mass = factor(n)
for i in mass:
	if i not in ans:
		ans.append(i)
		print(str(i) + ' ' + str(mass.count(i)))
