# 837 Перестановки
import itertools
mass=(input())
n=len(mass)
k=(list(itertools.permutations(mass, n)))

for i in k:
    print(*i, sep='')
