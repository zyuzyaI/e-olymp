# 2014 Счастливое число
n, m = input().split('.')
if n[0] == '-':
	n = n[1:]
print('Yes') if (sum(int(i) for i in n) == sum(int(i) for i in m)) else print('No')
