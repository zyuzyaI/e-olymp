# 910 Среднее арифметическое положительных
n1=int(input())
n=input().split()
c=[]
for i in n:
    i=float(i)
    if i>0:
        c.append(i)
if len(c)==0:
    print('Not Found')
else:
    k=float(sum(c)/len(c))
    print('%.2f' %k)
