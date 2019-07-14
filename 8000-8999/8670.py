# 8670 Степень двойки
n=int(input())
i=0
k=2
while True:
    k=2**i
    if k==n:
        print('YES')
        break
    elif k>n:
        print('NO')
        break
    i+=1
