# 109 Нумерація
def f(n):
    sehife = 0
    p = 9
    i = 1
    while True:
        if n <= i*p:
            if n%i != 0:
                return 0
            sehife = sehife+n/i
            return sehife
        n = n-p*i
        sehife = sehife + p
        p = p*10
        i += 1
n = int(input())
print(int(f(n)))
