# 5055 Количество дней от начала эры
from datetime import date
d = input()
d0 = date(1, 1, 1)
d1 = date(int(d[4:]), int(d[2:4]), int(d[:2]))
delta = d1 - d0
print (delta.days+1)
