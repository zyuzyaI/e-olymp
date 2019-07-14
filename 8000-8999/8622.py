# 8622 Делимость на цифры
n=int(input())
a1=n//1000
a2=(n//100)%10
a3=(n//10)%10
a4=n%10
k=0
if a1==0 or a2==0 or a3==0 or a4==0:
    k=1
else:
    if n%a1!=0 or n%a2!=0 or n%a3 or n%a4!=0:
        k=1

if k==1:
    print('NO')
if k==0:
    print('YES')
