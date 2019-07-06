# 028  Произведение
n=int(input())
i=1

while True:
    i+=1
    p=i
    k=i
    while True:
        p+=1
        k*=p
        if k>n:
            break
        if k==n:
            print(i,p)
            break
    if k==n:
            
            break