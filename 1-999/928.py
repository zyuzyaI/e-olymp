# 928 Сумма наибольшего и наименьшего
n1=int(input())
n=input().split()
c=[]
for i in range(n1):
    c.append(int(n[i]))
kmax=max(c)
kmin=min(c)

print(kmax+kmin)
