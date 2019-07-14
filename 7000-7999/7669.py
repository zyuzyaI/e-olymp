# 7669 Сходинки
n=input().split()
a=int(n[0])
b=int(n[1])
symbol=str(n[2])
if 0<=a-b<=1:
    print(a)
elif symbol=='W':
    print(b+1)
elif symbol=='S':
    print(b+2)
