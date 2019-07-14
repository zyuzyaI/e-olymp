# 6275 Удвоение
n=int(input())
if n<0:
    n=-n
    a=n//100
    b=(n//10)%10
    c=n%10
    print('-'+str(a)+str(a)+str(b)+str(b)+str(c)+str(c))
else:
    a=n//100
    b=(n//10)%10
    c=n%10
    print(str(a)+str(a)+str(b)+str(b)+str(c)+str(c))
