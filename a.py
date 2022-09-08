import sympy as sp
from sympy.core.symbol import Symbol 
import numpy as np
from scipy.optimize import fsolve
import numpy as np
def func(x):
    g=9.8
    rho=998.29
    mu=1.003e-3
    L1a=12.5
    L1b=12.5
    L2=25
    D1a=0.03
    D1b=0.06
    kLexp=0.5625
    D2=0.05
    pi=np.pi

    #x0=Hbomba
    #x1=Q
    #x2=hLT1
    #x3=hLT2
    #x4=v1a
    #x5=f1a
    #x6=v1b
    #x7=f1b
    #x8=v2
    #x9=f2
    #x10=Re1a
    #x11=Re1b
    #x12=Re2
    #x13=Q1a
    #x14=Q1b
    #x15=Q2                     
    
    return [0.48655-x[0]*x[1],
            7+x[2]-x[0],
            x[3]-x[2],
            (x[4]**2)/(2*g)*(x[5]*(L1a/D1a)+kLexp)+(x[6]**2)/(2*g)*(x[7]*(L1b/D1b))-x[2],
            (x[8]**2)/(2*g)*(x[9]*(L2/D2)) - x[3],
            -2*(np.log10(2.51/(x[10]*(x[5]**0.5)))) - x[5]**0.5,
            -2*(np.log10(2.51/(x[11]*(x[7]**0.5)))) - x[7]**0.5,
            -2*(np.log10(2.51/(x[12]*(x[9]**0.5)))) - x[9]**0.5,
            ((rho*x[4]*D1a)/mu) - x[10],
            ((rho*x[6]*D1b)/mu) - x[11],
            ((rho*x[8]*D2)/mu) - x[12],
            x[13]+x[15]-x[1],
            (pi/4)*(D1a**2)*x[4] - x[13],
            (pi/4)*(D1b**2)*x[6] - x[14],
            (pi/4)*(D2**2)*x[8] - x[15],
            x[14] - x[13]]




respuesta= fsolve((func), [10, 15, 10, 10, 1, 0.04, 1, 0.04, 1, 0.04, 20000, 20000, 20000, 10, 10, 10 ])
print(respuesta)