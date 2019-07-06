# 10 Садовник
n=int(input())
k=0
i=n
c=0
while c<=0.5:
    c=c+1/(i)
    i-=1
    k+=1
print(n-k+1)
