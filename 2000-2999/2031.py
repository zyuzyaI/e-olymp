# 2031 Последовательность чисел Фибоначчи
n=int(input())
a,b=1,1
print(1)
print(1)
for i in range(n-2):
    a,b=b,a+b
    print(b)
