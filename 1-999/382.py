# 382 Грушевое дерево
n,k,m = map(int, input().split())

while (n > 0):
 	if (n <= k):
 		k = n
 		n = n - k
 	else:
 		n = n - k
 		k = k + m

print(k)
