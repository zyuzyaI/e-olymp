# 8936 136
n, m  = map(int, input().split())
mass =[i for i in  range(n, m+1) if i % 2 == 0]
mass.sort(reverse=True)
print(*mass)
