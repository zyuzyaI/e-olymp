# 542 Поставка содовой воды
e, m, k = map(int, input().split())
count_b = 0
tmp = e+m
while (tmp // k) > 0:
	count_b += tmp // k
	tmp = tmp // k + tmp % k
print(count_b)
