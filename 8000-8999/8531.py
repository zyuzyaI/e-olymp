# 8531 Делимость на числа
q=input().split()
a=int(q[1])
n=int(q[0])
b=int(q[2])
if n%a==0 and n%b==0:
    print('YES')
else:
    print('NO')
