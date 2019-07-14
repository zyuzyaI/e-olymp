# 8524 Сумма положительных в матрице
n=int(input())

b=[]
for i in range(n):
    k=input().split()
    c=[int(j) for j in k]
    b.append(c)
k=0
for i in range(n):
    for j in range(n):
        if b[i][j]>0:
            k+=b[i][j]
print(k)
