# 8620 Три одинаковые цифры
n=input()
k=0
c=[]
for i in n:
    k=n.count(i)
    c.append(k)
if 3 in c:
    print('YES')
else:
    print('NO')
