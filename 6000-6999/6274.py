# 6274 Раздел клада
import math
n=input().split()
a,b=int(n[0]),int(n[1])
c=int(math.sqrt(1+8*(a-b)-1)/2)
print(c)
