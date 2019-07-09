# 1602 НОК двух натуральных чисел
def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
n=input().split()
a=int(n[0])
b=int(n[1])
print(lcm(a, b))
