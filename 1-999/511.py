# 511 Угадай число
n=input().split()
b,k=int(n[0]),int(n[1])
a=1

i=0
while 1:
    i+=1
    if (a+b)//2==k:

        print(i)
        break
    elif (a+b)//2<k:
        a=(a+b)//2+1


    elif (a+b)//2>k:
        b=(a+b)//2-1
