# 15 Мышка и зернышки
q=input().split()
n,m=int(q[0]),int(q[1])
mass=[]
x=[]
for i in range(n):
    c=[int(i) for i in input().split()]
    x.append(c)
    
for i in range(n-1,-1,-1):
    c=[]
    for j in range(m):
        c.append(x[i][j])
    mass.append(c)
ans=''
for i in range(1,n):
    mass[i][0]=mass[i][0]+mass[i-1][0]
for j in range(1,m):
    mass[0][j]=mass[0][j]+mass[0][j-1]
for i in range(1,n):
    for j in range(1,m):
        mass[i][j]=mass[i][j]+max(mass[i - 1][j], mass[i][j - 1])
                                              
k=n-1
t=m-1
while (k>0 or t>0):
    if (k>0 and t>0):
        if (mass[k-1][t]>mass[k][t-1]):
            ans+="F"
            k-=1
        else:
            ans+="R"
            t-=1
    elif (k==0):
        ans+="R"
        t-=1
    elif (t==0):
        ans+="F"
        k-=1
print(ans[::-1])