# 4730 Фибоначчи
from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
n=int(input())
print(int(F(n+1)))
