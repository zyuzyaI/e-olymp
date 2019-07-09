# 1612 Измените единицу
n=int(input())
b=bin(n)
c=b[::-1]
k=0
a=[]
for i in c:
    if i=='1':
        k+=1
        if k==1:
            a.append('0')
            continue
    a.append(i)
a=a[::-1]
v=''.join(a)
print(int(v,2))
