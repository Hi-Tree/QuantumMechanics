import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

κ = sp.Symbol("κ")
k = sp.Symbol("k")
E = sp.Symbol("E")
m_b = (9.109*10**(-31))*0.067
m_w = (9.109*10**(-31))*0.092
a = 1.2*10**(-9)
b = a + 6.4*10**(-10)
c = b+a
v = 9.1324*10**(-18)
h_b = 1.0545*10**(-34)

k_p = sp.sqrt((2*m_b*sp.Abs(v-E))/h_b**2)
kk = sp.sqrt((2*m_w*E)/h_b**2)

#OK

M1 = sp.Matrix([[1,1],[κ/m_b,-κ/m_b]])#ok
M2 = sp.Matrix([[0,1],[k/m_w,0]])
M3 = sp.Matrix([[sp.sin(k*a),sp.cos(k*a)],[(k/m_w)*sp.cos(k*a),(-k/m_w)*sp.sin(k*a)]])#ok
M4 = sp.Matrix([[sp.exp(κ*a),sp.exp(-κ*a)],[(κ/m_b)*sp.exp(κ*a),(-κ/m_b)*sp.exp(-κ*a)]])#ok
M5 = sp.Matrix([[sp.exp(κ*b),sp.exp(-κ*b)],[(κ/m_b)*sp.exp(κ*b),(-κ/m_b)*sp.exp(-κ*b)]])#ok
M6 = sp.Matrix([[sp.sin(k*b),sp.cos(k*b)],[(k/m_w)*sp.cos(k*b),(-k/m_w)*sp.sin(k*b)]])#ok
M7 = sp.Matrix([[sp.sin(k*c),sp.cos(k*c)],[(k/m_w)*sp.cos(k*c),(-k/m_w)*sp.sin(k*c)]])#ok
M8 = sp.Matrix([[sp.exp(κ*c),sp.exp(-κ*c)],[(κ/m_b)*sp.exp(κ*c),(-κ/m_b)*sp.exp(-κ*c)]])#ok


M = (M1**-1)*M2*(M3**-1)*M4*(M5**-1)*M6*(M7**-1)*M8
M22 = M[1,1]
#OK
i = np.linspace(0,v/2,1000)
g = M22.subs([(κ,k_p),(k,kk)]).evalf()
g_ = []
for N in i:
     z = float(g.subs(E,N).evalf())
     g_.append(z)
     
plt.plot(i,g_)
plt.plot(i,[0]*1000)
plt.xlabel("E")
plt.ylabel("M(2,2)(E)")
plt.show()
