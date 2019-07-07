# 339 Опять несократимые
n=int(input())
while n!=0:

    if n==0:
        break
    else:
        k = n
        i=2
        while i*i<=n:
            if (n % i == 0):
                while (n % i == 0):
                    n/= i
                k-=k/i
            i+=1

        if (n > 1):
            k-=k/n

        print(int(k))
    n=int(input())
