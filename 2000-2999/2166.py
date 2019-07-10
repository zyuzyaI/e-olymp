# 2166 Анаграммы
a=input()
a=list(a)
b=input()
b=list(b)
a.sort()
b.sort()
if a==b:
    print('YES')
else:
    print('NO')
