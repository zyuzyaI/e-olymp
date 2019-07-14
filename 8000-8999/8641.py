# 8641 Трехзначные числа Армстронга
n=input().split()
b=int(n[0])
c=int(n[1])

for i in range(b,c+1):
    if i==(((i//100)**3)+(((i//10)%10)**3)+((i%10)**3)):
        print(i, end=' ')
