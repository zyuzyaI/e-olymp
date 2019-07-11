# 2863 Нечетные делители
n=int(input())
c=[i for i in range(1,n+1) if (n%i==0 and i%2==1)]
for i in c:
    print(i)
