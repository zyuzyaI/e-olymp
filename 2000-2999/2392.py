# 2392 Интересная сумма
n=input()
c=[int(i) for i in n]
c.sort()
for i in range(1):
    if c[0]==0:
        if c[1]==0:
            c=[c[2],c[1],c[0]]
            print(int(n)*2)
        else:
            c=[c[1],c[0],c[2]]
            v_min=(str(c[0]),str(c[1]),str(c[2]))
            v_max=(str(c[2]),str(c[0]),str(c[1]))
            v1=int(''.join(v_min))
            v2=int(''.join(v_max))
            print(v1+v2)
    else:
        c_min=c
        c_max=c[::-1]
        our1=[str(i) for i in c_min]
        our2=[str(i) for i in c_max]
        w1=''.join(our1)
        w2=''.join(our2)
        print(int(w1)+int(w2))
