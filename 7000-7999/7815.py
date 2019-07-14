# 7815 Щедрый Вася
n1=input().split()
n,k=int(n1[0]),int(n1[1])
count=1
eat=0
while n>0:
    eat+=n%(k+1)
    n//=k+1
    count+=1
print(count, eat)
