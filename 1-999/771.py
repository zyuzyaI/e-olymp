# 771 Последовательность Фибоначчи
def f(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

print(f(int(input())))
