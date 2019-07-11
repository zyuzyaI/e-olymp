# 2862 Количество делителей
n=int(input())
c=[i for i in range(1,n+1) if n%i==0]
print(len(c))
