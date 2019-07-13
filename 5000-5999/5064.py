# 5064 Магическая контстанта
from math import sqrt
n=int(input())
k = int(((sqrt(8*n + 1) - 1)/2))
print(k if int(k*(k + 1)) == 2*n else -1)
