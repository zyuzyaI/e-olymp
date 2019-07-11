# 3551 Repeating Characters
q=int(input())
for i in range(q):
    n=input().split()
    print(n[0]+' ' ,end='')
    for i in n[2]:

        print(i*int(n[1]),sep='', end='')
    print()
