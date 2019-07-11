# 3732 Разящий тапок
n=int(input())
c=0
k=1
for i in range(1, n+1):
    k*=i
    c+=k
print(c)
