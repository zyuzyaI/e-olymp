# 5083 Сумма цифр
q=int(input())
n=input().split()
k=sum(int(i) for i in n[0])
c=0
for j in range(1,q):
    if sum(int(i) for i in n[j])<=k:
        k=sum(int(i) for i in n[j])
        c=j
print(n[c])
