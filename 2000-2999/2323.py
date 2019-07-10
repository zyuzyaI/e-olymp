# 2323 Числа из цифр
n=input()
c=sorted(n)
v=int(''.join(c))
num=int(''.join(c[::-1]))
print(v+num)
