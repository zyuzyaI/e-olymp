# 420 Из пушки на Луну
n=input().split()
x=int(n[0])
y=int(n[1])
yer=81/((x**2)+(y**2))
ay=1/(((384000 - x)** 2)+(y**2))
if yer==ay:
    print("Equal")
elif yer > ay:
    print("Earth")
else:
    print("Moon")
