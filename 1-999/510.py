# 510 Тосты
n=input().split()
a=int(n[0])
k=int(n[1])
if a<=k:
    if a==0:
        print(0)
    else:
        print(4)

else:
    if a%k==0:
        print(int((a/k)*4))
    elif a%k>k//2:
        print(int((a//k)*4)+4)
    else:
        print((int((a//k)*4)+2))
