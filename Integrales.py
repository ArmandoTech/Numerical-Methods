import sympy as sp
from sympy.abc import A,B,C,D,T

def integrar(f, T1, T2):
  return sp.integrate(f,(T,T1,T2))


if __name__=='__main__':
  
  T1=298.15
  T2=573
  A=3.470
  B=1.450e-3
  C=0
  D=0.121e5
  m=11.03
  R=8.31451

  f=R*(A+B*T+C*T**2+D*T**-2)
  Cp=float(integrar(f, T1, T2))
  Q= m*Cp
  
  print(Q)
  