# 049 Кот учёный
dani=input().split()
l=int(dani[0])
n=int(dani[1])
k=int(dani[2])
x1=[]
x2=[]
for i in range(n):
    xy=input().split()
    xi=(int(xy[0]),int(xy[1]))
    yi=(int(xy[2]),int(xy[3]))
    x1.append(xi)
    x2.append(yi)
m=0
for i in range(n):

    if (l*l)>=((x1[i][0])**2+(x1[i][1])**2) or (l*l)>=((x2[i][0])**2+(x2[i][1])**2):
       m+=1
    else:
        a=(x2[i][1]-x1[i][1])
        b=-(x2[i][0]-x1[i][0])
        c=x1[i][1]*(x2[i][0]-x1[i][0])-x1[i][0]*(x2[i][1]-x1[i][1])
        if c*c<=l*l*(a*a+b*b) and -c*b<=(b*b+a*a)*max(x2[i][1],x1[i][1]) and -c*b>=(b*b+a*a)*min(x2[i][1],x1[i][1]):
            m+=1
v=m//k
print(v+1)
