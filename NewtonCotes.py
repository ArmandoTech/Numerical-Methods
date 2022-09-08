import math
import numpy as np
from sympy import *
from scipy.integrate import quad

T=Symbol('T')
pi=np.pi
k=0.153
m=1500
Ts=320
D=0.25
Cp=0.53+0.0006*T-6.25e-6*T**2
Miu=30+0.09*T-0.00095*T**2
h=(0.023*k)

f=lambda T: (0.53+0.0006*T-6.25e-6*T**2)/((((0.023*0.153/0.25)*(4*1500/(pi*0.25*(30+0.09*T-0.00095*T**2)))**0.8)*((30+0.09*T-0.00095*T**2)*(0.53+0.0006*T-6.25e-6*T**2)/0.153)**0.33)*(Ts-T))
obj, err = quad(f, 20, 60)
L=1500/(D*pi)*obj
print(L)
