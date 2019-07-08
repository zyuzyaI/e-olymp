# 833 Треугольник и точка
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
C=[int(i) for i in input().split()]
Q=[int(i) for i in input().split()]
x=(A[0]-Q[0])*(B[1]-A[1])-(B[0]-A[0])*(A[1]-Q[1])
y=(B[0]-Q[0])*(C[1]-B[1])-(C[0]-B[0])*(B[1]-Q[1])
z=(C[0]-Q[0])*(A[1]-C[1])-(A[0]-C[0])*(C[1]-Q[1])
if (x>=0 and y>=0 and z>=0) or (x<=0 and y<=0 and z<=0):
    print('In')
else:
    print('Out')
