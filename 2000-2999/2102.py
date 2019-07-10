# 2102 Площадь
from math import ceil as ce
n_m_k=[int(i) for i in input().split()]
n=ce(n_m_k[0]/n_m_k[2])
m=ce(n_m_k[1]/n_m_k[2])
print(n*m)
