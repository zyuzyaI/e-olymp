# 835 Покер
n=input().split()
c=[int(i) for i in n]
b=set(c)
p=[]
for j in b:
    p1=c.count(j)
    p.append(p1)
p.sort()

if p==[1,1,1,1,1]:
    c.sort()
    if c[4]-c[3]==c[3]-c[2]==c[2]-c[1]==c[1]-c[0]==1:
        print('Straight')
    else:
        print('Nothing')
elif p==[1,1,1,2]:
    print('One Pair')
elif p==[1,2,3]:
    print('Two Pairs')
elif p==[5]:
    print('Impossible')
elif p==[1,4]:
    print('Four of a Kind')
elif p==[2,3]:
    print('Full House')
elif p==[1,1,3]:
    print('Three of a Kind')
elif p==[1,2,2]:
    print('Two Pairs')
