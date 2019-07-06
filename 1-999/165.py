# 165 Симетрія
from math import log, ceil
n = int(input())
i = 0
while n > 0:
    i = int(log(n,2))
    n = n-int(pow(2,i))

print((i)+1)
