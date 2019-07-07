# 349 Экономная домохозяйка
from math import pi
s,r = map(int, input().split())
s_cookie = pi*(r**2)
n = 0
while s>0:
    n += s//(2*r)**2
    if s//(2*r)**2==0:
        break
    s -= s_cookie*(s//(2*r)**2)
print(int(n))
