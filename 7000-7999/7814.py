# 7814 Двузначное число из трехзначного
n=int(input())
a=n//100
b=(n//10)%10
c=n%10
min = a*10 + b
if (a*10 + c) < min:
    min = a*10 + c;
if(b!=0 and b*10 + c < min):
    min = b*10 + c
print(min)
