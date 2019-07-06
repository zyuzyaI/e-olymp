# 140 Фінансова піраміда
n = int(input())
b = 2
y = 2
a = 2
i = 2
while i <= n:
    a = a*2
    q = int((b+a)/2)
    b = int(b+a-q)
    y = int(a-q)
    i += 1
print('%d %d' %(y, b))
