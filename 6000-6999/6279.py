# 6279 Количество дней в месяце
import calendar
n=input().split()
year, mounth=int(n[1]),int(n[0])
b=calendar.monthrange(year, mounth)
print(b[1])
