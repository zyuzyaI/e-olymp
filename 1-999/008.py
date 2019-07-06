# 8 Спички
import math
n=int(input())
wigth=int(math.sqrt(n))
length=int(n/wigth)
ost=n-wigth*length
k=wigth*(length+1)+length*(wigth+1)
if ost!=0:
    k=k + 2 * ost + 1
print(k)