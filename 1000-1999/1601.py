# 1601 НОД двух чисел
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

n=input().split()
a=int(n[0])
b=int(n[1])


c=gcd(a,b)
print(c)
