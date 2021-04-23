import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#given the origin of the well at z = 0 for symmetry

m_g = 0.067*9.109*10**(-31)
h_b = 6.63*10**(-34)
v = 9.13241*10**(-18)
d_2 = 1.2*10**(-9)

x = np.linspace(0,2*np.pi, 1000)
y = x*np.tan(x)
y2 = -x/(np.tan(x))
y2[:-1][np.diff(y2) < 0] = np.nan
y[:-1][np.diff(y) < 0] = np.nan

z = np.sqrt((2*m_g*v*d_2**2)/(h_b**2))
a = z*np.cos(x)
b = z*np.sin(x)


plt.plot(a,b)
plt.plot(x, y2, label = "Odd")
plt.plot(x,y, label = "Even")
plt.ylim(0,3)
plt.xlim(0,8)

plt.legend()
plt.show()

