# 354 Перестановка
n=[int(i) for i in (input().split())]
a=n[0]
n=n[1:]
k=0
for i in range(1,a+1):
    if i in n:
        k+=1
        pass
    else:
        print(i)
        break
if k==len(n):
    print(0)
