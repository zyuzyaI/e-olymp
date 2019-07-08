# 905 Какой треугольник?
a,b,c=input().split()
if a==b or a==c or b==c:
    if a==b and b==c:
        print('1')
    else:
        print('2')

else:
    print('3')
