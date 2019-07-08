# 421 Йо-йо
n=input().split()
long,k=int(n[0]),int(n[1])
c=0
while True:
    long/=k
    if long<=1:
        break
    c+=1
print(c)
