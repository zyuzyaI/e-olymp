# 1119 Пирамида из символов
q=input().split()
a,n=str(q[0]),int(q[1])
k=((2+3*(n-1))*n)//2
print(k)
for i in range(1,n+1):
    print(' '*(n-i)+a*i+a*(i-1))
