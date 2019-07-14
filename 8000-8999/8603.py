# 8603 Сумма и произведение 3
n=int(input())
c=[]
for i in range(3):
    a=n%10
    n=n//10
    c.append(a)
k1=sum(c)
k2=c[0]*c[1]*c[2]
print(k1, k2)
