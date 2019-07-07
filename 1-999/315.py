# 315 Последствия рыбалки
n = int(input())
for i in range(n):
    q=input()
    a=[]
    b=[]
    k=True

    for j in q:
        if j  in ('+','-','*') :
            k=False
        if k:
            a.append(j)
        else:
            b.append(j)
    num1=''.join(a)
    num2=''.join(b)
    if b[0]=='*':
        mov=int(num1)*int(num2[1:])
        c=max(len(str(mov)),len(num1),len(num2))
        print(' '*(c-len(a))+num1)
        print(' '*(c-len(b))+num2)
        print('-'*c)
        if len(num2[1:])==1:

            print(' '*(c-len(str(mov)))+str(mov))
            print()
        else:
            d=0
            for z in num2[::-1]:
                if d==len(num2[1:]):
                    break
                print(' '*(c-len(str(int(num1)*int(z)))-d)+str(int(num1)*int(z)))
                d+=1
            print('-'*c)
            print(' '*(c-len(str(mov)))+str(mov))
            print()
    else:
        if b[0]=='+':
            mov=int(num1)+int(num2[1:])
            c=max(len(str(mov)),len(num1),len(num2))

            print(' '*(c-len(a))+num1)
            print(' '*(c-len(b))+num2)
            print('-'*c)
            print(' '*(c-len(str(mov)))+str(mov))
            print()

        elif b[0]=='-':
            mov=int(num1)-int(num2[1:])
            c=max(len(str(mov)),len(num1),len(num2))

            print(' '*(c-len(a))+num1)
            print(' '*(c-len(b))+num2)
            print('-'*c)
            print(' '*(c-len(str(mov)))+str(mov))
            print()
