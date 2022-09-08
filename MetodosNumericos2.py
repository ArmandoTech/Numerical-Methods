
from sympy.core.symbol import Symbol 
import numpy as np
from scipy.optimize import fsolve


def func(x):
    # x0=hla
    # x1=hlb
    # x2=QA
    # x3=Qb
    # x4=Va
    # X5=Vb
    # x6=fa
    # x7=fb
    # x8=Rea
    # x9=Reb

   pi=np.pi
   g=9.8
   rho=800
   mu=0.1
   La=500
   Lb=804.5
   Da=0.3046
   Db=0.45
   KL=0.3
   Q=3
   E=4.5e-5
   return   [x[0]-x[1],
            x[2]+x[3] - Q,
            x[4]*(pi/4)*Da**2 - x[2],
            x[5]*(pi/4)*Db**2 - x[3],
            (x[4]**2/(2*g))*(x[6]*(La/Da)+2*KL) - x[0],
            (x[5]**2/(2*g))*(x[7]*(Lb/Db)+2*KL) - x[1],
            0.25/(np.log10(E/(Da*3.7) + 5.74/x[8]**0.9)**2) - x[6],
            0.25/(np.log10(E/(Db*3.7) + 5.74/x[9]**0.9)**2) - x[7],
            (rho*x[4]*Da)/mu - x[8],
            (rho*x[5]*Db)/mu - x[9]]
    


respuesta= fsolve((func), [100, 100, 100, 100, 100, 100, 0.05, 0.05, 5000, 5000])
print(respuesta)