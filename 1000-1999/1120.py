# 1120 Четырехугольник
def f(x1, x2, y1, y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5

n = int(input())
for i in range(1,n+1):
	xa, ya, xb, yb, xc, yc, xd, yd = map(int, input().split())
	AB = f(xa, xb, ya, yb)
	BC = f(xb, xc, yb, yc)
	CD = f(xc, xd, yc, yd)
	DA = f(xd, xa, yd, ya)
	AC = f(xa,xc, ya, yc)
	DB = f(xd, xb, yd, yb)
	if AB == CD == BC == DA:
		if AC == DB:
			print('Case '+str(i)+': '+'Square')
		else:
			print('Case '+str(i)+': '+'Rhombus')
	else:
		if AB == CD and BC == DA:
			print('Case '+str(i)+': '+'Rectangle')
		else:
			print('Case '+str(i)+': '+'Other')
