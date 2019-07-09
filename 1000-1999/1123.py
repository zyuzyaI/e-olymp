# 1123 Счастливые числа
n=int(input())
for i in range(n):
    k=input()
    c=len(k)
    k1=int(k)
    k=int(k)
    spis=[]
    for j in range(c):
        chys=k1%10
        k1=k1//10
        spis.append(chys)
    sum1, sum2 = 0, 0
    for j in spis:
        sum1+=j
        sum2+=j*j
    if k%8==0 or sum1%8==0 or sum2%8==0:
        print('Lucky number!')
    else:
        print('What a pity!')
