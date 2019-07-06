# 126 Номер квартири
w = input().split()
n = int(w[0])
p = int(w[1])
q = int(w[2])
k = int(w[3])

flatEntrance = n/p
flatFloor = n/p/q
entrance = k/flatEntrance
if (k%flatEntrance != 0):
    entrance+=1
if (k%flatEntrance == 0):
    floor = q
else:
    floor = (k%flatEntrance)/flatFloor
    if (k%flatFloor != 0):
        floor += 1

print(int(entrance), int(floor))
