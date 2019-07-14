# 8623 Хотя бы две одинаковые цифры
n=int(input())
a1=n//10000
a2=(n//1000)%10
a3=(n//100)%10
a4=(n//10)%10
a5=n%10
k=0
if a1==a2 or a1==a3 or a1==a4 or a1==a5:
    k=1
if a2==a3 or a2==a4 or a2==a5:
    k=1
if a3==a4 or a3==a5:
    k=1
if a4==a5:
    k=1
if k==1:
    print('YES')
if k==0:
    print('NO')
