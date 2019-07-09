# 915 Прямоугольный или нет?
n1=input().split()
a=int(n1[0])
b=int(n1[1])
c=int(n1[2])
k=[a, b, c]
k.sort()
i=1
while i<=k[0]:
    if k[0]/i==3 and k[1]/i==4 and k[2]/i==5:
        print('YES')
        break
    i+=1
else:
    print("NO")
