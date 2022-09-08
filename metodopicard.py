import numpy as np

def calcular_error(xo, intentos):
    x=xo + (xo**3+3*xo**2-1)
    error=abs(x-xo)
    print(f'{intentos} xo={xo}   Error={error}')
    

    if error > 0.00001:
        x1=x + (x**3+3*x**2-1)
        calcular_error(x1, intentos + 1)
        
    return error, intentos 


if __name__=='__main__':
    calcular_error(-2.5 ,1)