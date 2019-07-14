# 7338 Постоянная сумма цифр
n=int(input())
m=0
for i in range(10,100):
    k=i//10+i%10
    c=str(i*n)
    b=sum(int(j) for j in c)
    if k==b:
        m+=1
print(m)
