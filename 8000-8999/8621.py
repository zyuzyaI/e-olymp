# 8621 Две одинаковые цифры
n=int(input())
a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10
if a==c and b==d and a!=d:
    print('YES')
elif a==b and c==d and a!=d:
    print('YES')
elif a==d and c==b and a!=b:
    print('YES')
else:
    print('NO')
