# 029 Уровень палиндромности
n=input()
n=''.join(n.split())
k=0
c=len(n)
q=0

while n!=n[::-1]:
    q=int(n)+int(n[::-1])
    q=str(q)
    n=q
    k+=1
print(k)