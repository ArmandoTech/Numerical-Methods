import numpy as np
import sympy as sym
from sympy import *

xi=np.array([5, 6, 7, 8])
fi=np.array([287.43, 295.13, 304.22, 312.59])
valor_interpolar=7 # VALOR QUE SE VA A EVALUAR EN LA DERIVADA

# PROCEDIMIENTO
# Polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)
for i in range(0,n,1):
    
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = sym.lambdify(x,polisimple)

print('Polinomio de Lagrange: ')
print(polisimple)

Derivada_Polinomio=Derivative(polisimple, x).doit()
Polinomio_Evaluado= sym.lambdify(x, Derivada_Polinomio)
print('\n')
print('Valor de la derivada mediante lagrange: ')
print(Polinomio_Evaluado(valor_interpolar))