# Санта Клаус 1494
n, m , k = map(int, input().split())
bag_1 = [int(i) for i in input().split()]
bag_2 = [int(i) for i in input().split()]
print(n - m - k)
print(*([i for i in range(1, n+1) if i not in  bag_1 and i not in bag_2 ]))