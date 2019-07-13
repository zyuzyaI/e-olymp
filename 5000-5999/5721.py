# 5721 Поиск элемента
q=input().split()
n=[int(i)  for i in input().split()]
n.sort()
n=n[::-1]
if int(q[1])>len(n):
    print(-1)
else:
    print(n[int(q[1])-1])
