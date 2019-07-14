# 8628 Все цифры четные
n=input()
c=0
n=int(n)
for i in range(4):
    k1=n%10
    n=n//10

    if k1%2==0:
        c+=1
if c==4:
    print('YES')
else:
    print('NO')
