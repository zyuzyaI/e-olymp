# 8697 Квадратная строка
n=input()
c=len(n)//2
if n[:c]==n[c:]:
    print('yes')
else:
    print('no')
