# 1127 Большое число
import math

q=int(input())
for i in range(q):
    n=int(input())
    if n<2:
        print(1)
    else:
        print(math.ceil(math.log10(2*math.pi*n)/2+n*(math.log10(n/math.e))))
