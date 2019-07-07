# 260 Тыквенная каша
n=[int(i) for i in input().split()]
q=n[1:]
q.sort()
print(*q[::-1])
