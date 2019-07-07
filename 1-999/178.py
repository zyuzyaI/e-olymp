# 178 Кожен третій безкоштовно
while True:
    q,n = map(int,input().split())
    if q == 0 and n == 0:
        break
    else:
        print(int(q/(n-q)+1))
