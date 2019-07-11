# 3258 Последовательность Фибоначчи
n=int(input())
fib1=1
fib2=1
i=2
if 0<n<=2:
    fib_sum=1
elif n==0:
    fib_sum=0
while i<n:
    fib_sum=fib1+fib2
    fib1=fib2
    fib2=fib_sum
    i+=1
print(fib_sum)
