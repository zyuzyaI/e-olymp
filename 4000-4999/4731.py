# 4731 Количество элементов, равных максимуму
n=[]
while True:
    c=int(input())
    if c==0:
        break
    n.append(c)
print(n.count(max(n)))
