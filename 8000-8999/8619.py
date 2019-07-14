# 8619 Пятизначное по порядку
n=int(input())
n1=n//10000
n2=(n//1000)%10
n3=(n//100)%10
n4=(n//10)%10
n5=n%10
if n1<n2<n3<n4<n5:
    print('YES')
else:
    print('NO')
