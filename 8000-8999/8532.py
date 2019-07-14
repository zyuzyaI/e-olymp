# 8532 Печать квадратов и кубов
q=input().split()
a=int(q[1])
n=int(q[0])
for i in range(n,a+1):
    print(i**2, end=' ')

print()
for i in range(a,n-1,-1):
    print(i**3, end=' ')
