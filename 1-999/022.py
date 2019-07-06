# 22 "Зеркально простые" числа
n=input().split()
w,e=int(n[0]), int(n[1])
a=[True]*10001
a[0]=a[1]=False
for k in range(2,10001):
    if a[k]:
        for m in range(2*k,10001,k):
            a[m]=False
q=0
for i in range(min(w,e),max(e,w)+1):
    i=str(i)
    if a[int(i)] and a[int(i[::-1])]:
        q+=1
print(q)