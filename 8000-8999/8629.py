# 8629 Хотя бы одна нечетная
n=input()
k2=len(n)
c=0
n=int(n)
for i in range(k2):
    k1=n%10
    n=n//10

    if k1%2!=0:
        c=1
if c==1:
    print('YES')
else:
    print('NO')
