# 4727 Второе вхождение
s = input()
k=0
c=0
for i in s:
    if i=='f':
        k+=1
    if k==2:
        print(c)
        break
    c+=1
if k==1:
    print(-1)
elif k==0:
    print(-2)
