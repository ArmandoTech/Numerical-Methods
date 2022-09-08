import numpy as np
import sympy as sp
from sympy.core.symbol import Symbol 
from sympy import *

def derivada(y):
	x= Symbol('x')
	return Derivative(y, x).doit()
    

def calcular_error(y, y_prima, x, tolerancia, intentos):
    
    

    x1=x - y(x)/y_prima(x)

    error=abs(x1-x)
    print(f'{intentos} xo={x}   Error={error}')
    

    if error > tolerancia:
        
        x2=x1 - y(x1)/y_prima(x1) 
        calcular_error(y, y_prima, x2, tolerancia, intentos + 1)
        
    return error, intentos


if __name__=='__main__':
    

    y=input("Función: ")
    x=float(N((input("Valor inicial: "))))
    tolerancia=float(input("Tolerancia: "))

    intentos=1

    y_prima= derivada(y)
    
    

    y=sp.lambdify(Symbol('x'), y)
    y_prima=sp.lambdify(Symbol('x'), y_prima)

    calcular_error(y, y_prima, x, tolerancia, intentos)
    
    