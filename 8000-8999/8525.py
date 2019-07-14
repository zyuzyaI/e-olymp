# 8525 Четные отрицательные в матрице
n=int(input())

b=[]
for i in range(n):
    k=input().split()
    c=[int(j) for j in k]
    b.append(c)
k=0
a=0
for i in range(n):
    for j in range(n):
        if b[i][j]<0 and  b[i][j]%2==0:
            k+=b[i][j]
            a+=1
print(a,k)
