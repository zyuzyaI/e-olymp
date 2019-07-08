# 903 Первая или последняя?
c=int(input())

if c//100>c%10:
    print(c//100)
elif c//100<c%10:
    print(c%10)
else:
    print('=')
