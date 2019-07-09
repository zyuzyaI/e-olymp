# 933 Сумма цифр двуцифрового числа
n=int(input())
if n<0:
  n=-n
  a1=(n//10)
  a2=n%10

else:
  a1=n//10
  a2=(n%10)
print(a1+a2)
