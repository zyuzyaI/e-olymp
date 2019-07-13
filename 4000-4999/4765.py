# 4765 Удаление дублей из сортированного массива
from itertools import groupby


n1=int(input())
n=input().split()
new_x = [el for el, _ in groupby(n)]


for i in new_x:
    print(i, end=' ')
