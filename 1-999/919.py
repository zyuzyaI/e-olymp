# 919 Номер на 3
n=int(input())
n1=input().split()
c=[]
for i in range(n):
    if (i+1)%3==0:
        if float(n1[i])>0:
            c.append(float(n1[i]))

k=sum(c)
k1=len(c)
print('%d %.2f' %(k1,k))
