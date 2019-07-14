# 7369 Километровые столбы (Mileposts)
n=input().split()
a=int(n[0])
b=int(n[1])
while a%7!=3:
    a+=1
k=(b+4)/7-(a+4)/7+(a%7==3)
print(int(k))
