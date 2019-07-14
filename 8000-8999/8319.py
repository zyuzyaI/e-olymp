# 8319 Простой калькулятор
m=input().split()
a, x, b= int(m[0]), str(m[1]), int(m[2])
if x=='-':
    print(a-b)
elif x=='+':
    print(a+b)
elif x=='*':
    print(a*b)
else:
    print(a//b)
