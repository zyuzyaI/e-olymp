# 177 Покер
def f(n):
    n.sort()
    a = [n.count(n[0])]
    for i in range(1,5):
        if n[i-1] != n[i]:
            a.append(n.count(n[i]))
    if len(a) == 1:
        print("poker")
    elif len(a) == 2:
        if 3 in a:
            print("full house")
        else:
            print("quads")
    elif len(a) == 5:
        print("no pair")
    elif len(a) == 3:
        if 3 in a:
            print('set')
        else:
            print("two pair")
    else:
        print("pair")


q = int(input())
for i in range(q):
    n = [i for i in input().split()]
    f(n)
