
import numpy as np
import sympy as sp
from sympy.core.symbol import Symbol 

def FL(p):

    A = np.array([
        [1, 1, 1], 
        [1, 5, 25], 
        [1, 20, 20**2]])

    b = np.array([56.5, 113, 181])

    A_inversa = np.linalg.inv(A)
    x = np.dot(A_inversa, b)

    FL= x[0]+x[1]*p+x[2]*p**2 #Funcion de interpolación
    return FL
    
if __name__=='__main__':
    T=FL(2)  #Se evalúa en el valor de presión deseado
    print(T)