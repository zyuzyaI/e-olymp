#6956 Статистика Дней Рождений

n = int(input())
dct = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
for i in range(n):
	b = input().split('/')

	dct[int(b[1])] += 1
for i, j in dct.items():
	print(i, j)
