# 921 Отрицательные элементы
n=int(input())
n1=input().split()

c=[]
for i in n1:
    i=float(i)
    if i<0:
        c.append(i)
k=sum(c)
k1=len(c)
print('%d %.2f' %(k1, k))
