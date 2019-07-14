# 7816 Два поезда
n=input().split()
a,b=int(n[0]),int(n[1])
c=(60*(a*a/b))
print(int(c//60), int(c%60))
