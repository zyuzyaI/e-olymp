# 8618 Четырехзначный палиндром
n=int(input())
n1=n//1000
n2=(n//100)%10
n3=(n//10)%10
n4=n%10
if n4==n1 and n2==n3:
    print('YES')
else:
    print('NO')
