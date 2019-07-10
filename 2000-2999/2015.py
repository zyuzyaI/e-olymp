# 2015 Игра XOR
n  = int(input())
mass = sum(int(i) for i in input().split())
print('First') if mass%2 == 0 else print('Second')
