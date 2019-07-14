# 8696 Оценки
n=input()
a2=n.count('2')
a5=n.count('5')
if a2==a5:
    print('=')
elif a2<a5:
    print(5)
else:
    print(2)
