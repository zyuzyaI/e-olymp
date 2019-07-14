# 8280 Количество четных делителей
n=int(input())
k=0
for i in range(1,n+1):
    if n%i==0 and i%2==0:
        k+=1

print(k)
