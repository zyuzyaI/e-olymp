# 8317 Квадрат разности
n=input()
c=[i for i in n]
c.sort()
a=c[::-1]

a=''.join([i for i in a])
c=''.join([i for i in c])

print((int(a)-int(c))**2)
