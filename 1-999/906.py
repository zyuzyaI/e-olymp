# 906 Произведение цифр
n=int(input())
c=[]
for i in range(3):
    n1=n%10
    c.append(n1)
    n=n//10
print(c[0]*c[1]*c[2])
