# 916 Интересное произведение
n1=input().split()
a=int(n1[0])
b=int(n1[1])
c=int(n1[2])
d=int(n1[3])
k1=0
c1=[]
if a<b:
    if c<d:
        for i in range(a,b+1):
            for j in range(c,d+1):
                k1=i*j
                if k1 in c1:
                    pass
                else:
                    c1.append(k1)
    else:
        for i in range(a,b+1):
            for j in range(d,c+1):
                k1=i*j
                if k1 in c1:
                    pass
                else:
                    c1.append(k1)
else:
    if c<d:
        for i in range(b,a+1):
            for j in range(c,d+1):
                k1=i*j
                if k1 in c1:
                    pass
                else:
                    c1.append(k1)
    else:
        for i in range(b,a+1):
            for j in range(d,c+1):
                k1=i*j
                if k1 in c1:
                    pass
                else:
                    c1.append(k1)





print(len(c1))
