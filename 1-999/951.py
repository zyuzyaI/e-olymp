# 951 Обмен
n=int(input())

a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10
m=[a,c,b,d]
for i in m:
    print(i, end='')
