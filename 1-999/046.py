# 046 Отрезки
n=int(input())
a=[0,1,1]+[0]*48
for i in range(3,48):
    a[i]=a[i-1]+a[i-2]
cem=0
j=1
while (cem<=n):
    cem=cem+a[j]
    j+=1
print(j-2)
