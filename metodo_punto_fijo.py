import numpy as np
    
def calcular_error(xo, intentos):
    x=xo - (xo-0.8-0.2*np.sin(xo))/(1-0.2*np.cos(xo))
    error=abs(x-xo)
    print(f'{intentos} xo={xo}   Error={error}')
    

    if error > 0.00001:
        x1=x-(x-0.8-0.2*np.sin(x))/(1-0.2*np.cos(x))
        calcular_error(x1, intentos + 1)
        
    return error, intentos 


if __name__=='__main__':
    calcular_error((np.pi)/4, 1)

