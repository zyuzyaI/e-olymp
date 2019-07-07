# 200 Чотирикутник - 2
def f(a,b):
    A=(a[0]-b[0])**2+(a[1]-b[1])**2
    return A
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
d=[int(i) for i in input().split()]
AB=f(a,b)
AC=f(a,c)
AD=f(a,d)
BD=f(b,d)
BC=f(b,c)
CD=f(c,d)
if AB==CD and AC==BC and BC==BD and BD==AD and AC+BC==AB:
    print('YES')
elif AC==BD and AB==BC and BC==CD and CD==AD and AB+BC==AC:
    print('YES')
elif AD==BC and AB==BD and BD==CD and CD==AC and AB+BD==AD:
    print('YES')
else:
    print('NO')
