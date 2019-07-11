# 4744 Шестерёнки
def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
a, b = map(int, input().split())
print(lcm(a,b))
