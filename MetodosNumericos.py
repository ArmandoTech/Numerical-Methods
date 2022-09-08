import numpy as np
import sympy as sp
from sympy.core.symbol import Symbol 
from sympy import *
import matplotlib.pyplot as plt

def derivada(y):
	x= Symbol('x')
	return Derivative(y, x).doit()
    
def segunda_derivada(y_prima):
    x= Symbol('x')
    return Derivative(y_prima, x).doit()

def MetodoNewton(y, y_prima, x, tolerancia, intentos):
    
    
    x1=x - y(x)/y_prima(x)

    error=abs(x1-x)
    print(f'{intentos} xo={x}   Error={error}')
    

    if error > tolerancia:
        
        x2=x1 - y(x1)/y_prima(x1) 
        MetodoNewton(y, y_prima, x2, tolerancia, intentos + 1)
        
    return error, intentos

def MetodoHalley(y, y_prima, y2_prima, x, tolerancia, intentos):
    H=(y(x)* y2_prima(x))/(y_prima(x))**2
    x1=x-((2/(2-H))*(y(x)/y_prima(x)))
    error=abs(x1-x)
    print(f'{intentos} xo={x}   Error={error}')

    if error > tolerancia:
        x2=x1-((2/(2-H))*(y(x1)/y_prima(x1)))
        MetodoHalley(y, y_prima, y2_prima, x2, tolerancia, intentos + 1)
    
        

def MetodoMuller(y, y_prima, y2_prima, x, tolerancia, intentos):
    
    M= (y(x)*y2_prima(x))/(y_prima(x))**2
    criterio=y_prima(x)

    if isinstance(criterio, complex):
        criterio=criterio.real
    

    if criterio > (0):
        x1= -(2/(1+(1-2*M)**0.5))*(y(x)/abs(y_prima(x)))+ x
        error=abs(x1-x)
        print(f'{intentos} xo={x}   Error={error}')
        if error > tolerancia:
              
            criterio2=y_prima(x1)
            if isinstance(criterio, complex): 
                criterio2=criterio2.real

            x2= -(2/(1+(1-2*M)**0.5))*(y(x1)/abs(y_prima(x1))) + x1
            MetodoMuller(y, y_prima, y2_prima, x2, tolerancia, intentos + 1)

    else:
        x1= (2/(1+(1-2*M)**0.5))*(y(x)/abs(y_prima(x)))
        error=abs(x1-x)
        print(f'{intentos} xo={x}   Error={error}')
        if error > tolerancia:  
            x2= (2/(1+(1-2*M)**0.5))*(y(x1)/abs(y_prima(x1)))
            MetodoMuller(y, y_prima, y2_prima, x2, tolerancia, intentos + 1)


def MetodoAitkenSteffensen(y, x, tolerancia, intentos):
    x1=x+y(x)
    error=abs(x1-x)
    print(f'{intentos} xo={x} Error={error}')
    if error > tolerancia:
        p0=x
        p1=y(p0)+p0
        p2=y(p1)+p1 
        x2=p2 - (p1-p2)**2/(p2-2*p1+p0)

        MetodoAitkenSteffensen(y, x2, tolerancia, intentos + 1)


#SE DEBE GRAFICAR AHORA LA DERIVADA EVALUADA EN EL PUNTO 1, DEBE ESTAR ENTRE -1 Y 1 
#SE DEBEN TRAZAR LINEAS PARALELAS EN -1 Y 1 PARA PODER ESCOGER EL PUNTO INICIAL


if __name__=='__main__':
    
    Metodo=input("Método: ")

    if Metodo == 'Newton':   #METODO NEWTON

        y=input("Función: ")
        x=float(N((input("Valor inicial: "))))
        tolerancia=float(input("Tolerancia: "))

        intentos=1

        y_prima= derivada(y)
        y2_prima= segunda_derivada(y_prima)
        

        y=sp.lambdify(Symbol('x'), y)
        y_prima=sp.lambdify(Symbol('x'), y_prima)
        y2_prima=sp.lambdify(Symbol('x'), y2_prima)


        convergencia= abs(y(x)* y2_prima(x)/(y_prima(x))**2)
        if convergencia < 1:
            MetodoNewton(y, y_prima, x, tolerancia, intentos)
        else:
            print("Ingrese otro punto inicial ")
           


    elif Metodo == 'Halley':   #METODO HALLEY

        y=input("Función: ")
        x=float(N(input("Valor inicial: ")))
        tolerancia=float(input("Tolerancia: "))

        intentos=1

        y_prima= derivada(y)
        y2_prima= segunda_derivada(y_prima)


        y=sp.lambdify(Symbol('x'), y)
        y_prima=sp.lambdify(Symbol('x'), y_prima)
        y2_prima=sp.lambdify(Symbol('x'), y2_prima)
        convergencia= abs(y(x)* y2_prima(x)/(y_prima(x))**2)
        if convergencia < 1: 

            MetodoHalley(y, y_prima, y2_prima, x, tolerancia, intentos)

        else:
            print("Ingrese otro punto inicial ")


    elif Metodo == 'Muller':     #METODO MULLER

        y=input("Función: ")
        x=float(N(input("Valor inicial: ")))
        tolerancia=float(input("Tolerancia: "))

        intentos=1

        y_prima= derivada(y)
        y2_prima= segunda_derivada(y_prima)

        y=sp.lambdify(Symbol('x'), y)
        y_prima=sp.lambdify(Symbol('x'), y_prima)
        y2_prima=sp.lambdify(Symbol('x'), y2_prima)

        convergencia= abs(y(x)* y2_prima(x)/(y_prima(x))**2)

        if convergencia < 1:

            MetodoMuller(y, y_prima, y2_prima, x, tolerancia, intentos)

        else:
            print("Ingrese otro punto inicial")
            

    elif Metodo == 'AS':
        y=input("Función: ")  
        x=float(N(input("Valor inicial: ")))
        tolerancia=float(input("Tolerancia: "))

        intentos=1

        y=sp.lambdify(Symbol('x'), y)

        MetodoAitkenSteffensen(y, x, tolerancia, intentos)