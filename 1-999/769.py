# 769 Прямоугольник
def X(x1,x2,x3):
	if x1 == x2:
		return x3
	elif x1 == x3:
		return x2
	else:
		return x1

def Y(y1,y2,y3):
	if y1 == y2:
		return y3
	elif y1 == y3:
		return y2
	else:
		return y1

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(X(x1,x2,x3), Y(y1,y2,y3))
