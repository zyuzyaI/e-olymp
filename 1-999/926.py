# 926 Формула Герона
n=input().split()
c=[]
for i in n:
    c.append(float(i))
a,b,c,d,f=c

p1=(a+b+f)/2
p2=(c+d+f)/2

s1=((p1*(p1-a)*(p1-b)*(p1-f))**0.5)
s2=((p2*(p2-c)*(p2-d)*(p2-f))**0.5)

print('%.4f' %(s1+s2))
