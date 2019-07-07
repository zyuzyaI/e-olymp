# 255 Лицензионное ПО
n=0
c=input()
for i in c:
    i=int(i)
    n+=i
if n==0:
    print(0)
else:

    k=(n-1)%9+1
    print(k)
