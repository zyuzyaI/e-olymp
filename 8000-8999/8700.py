# 8700 Мода
a1,a2,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,0
while True:
    n=int(input())
    if n==0:
        break
    elif n==1:
        a1+=1
    elif n==2:
        a2+=1
    elif n==3:
        a3+=1
    elif n==4:
        a4+=1
    elif n==5:
        a5+=1
    elif n==6:
        a6+=1
    elif n==7:
        a7+=1
    elif n==8:
        a8+=1
    elif n==9:
        a9+=1
c=max(a1,a2,a3,a4,a5,a6,a7,a8,a9)
if c==a1:
    print(1)
    print(a1)
elif c==a2:
    print(2)
    print(a2)
elif c==a3:
    print(3)
    print(a3)
elif c==a4:
    print(4)
    print(a4)
elif c==a5:
    print(5)
    print(a5)
elif c==a6:
    print(6)
    print(a6)
elif c==a7:
    print(7)
    print(a7)
elif c==a8:
    print(8)
    print(a8)
elif c==a9:
    print(9)
    print(a9)
