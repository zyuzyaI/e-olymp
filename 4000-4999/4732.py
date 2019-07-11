# 4732 Иччанобиф
n=int(input())

a,b=1,1
i=1
while b!=n:
    i+=1
    a,b=b,a+b
print(i)
