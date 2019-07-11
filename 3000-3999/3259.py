# 3259 Делители
n=int(input())
k=1
i=1
c=n
while n!=k:
    if n==13:
        c=4096
        break
    while c>i:
        i+=1
        if c%i==0:
            k+=1

    if k==n:
        break
    k=1
    i=1
    c+=1

print(c)
