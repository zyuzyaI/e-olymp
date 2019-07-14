# 7363 Сумма дробей
def div(x,y):
    while x*y!=0:
        if (x<y):
            y=y%x
        else:
            x=x%y
    return x + y

n=[int(i) for i in (input().split())]
a,b,c,d=int(n[0]),int(n[1]),int(n[2]),int(n[3])
suret=int(a*d+b*c)
mexrec=b*d
ebob=div(suret, mexrec)
suret=int(suret/ebob)
mexrec=int(mexrec/ebob)

if (mexrec == 1):
    print(suret)
else:
    print(suret, mexrec)
