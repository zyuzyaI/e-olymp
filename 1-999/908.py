# 908 Те, что делятся на 6
n1=int(input())
n=input().split()
c=[]
c1=[]
for i in n:
    i=int(i)
    if i>0:
        c.append(i)
for i in c:
    if i%6==0:
        c1.append(i)
print(len(c1), sum(c1))
