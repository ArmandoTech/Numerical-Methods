
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    func = t/2 - y
    return func

def euler(t0, y0, h, n):
    t=np.zeros(n+1)
    y=np.zeros(n+1)
    t[0]=t0
    y[0]=y0
    print('y(' , t, ')=', y)
    for k in range(n):
        y[k+1]=y[k]+h*f(t[k],y[k])
        t[k+1]=t[k]+h
        print('y(' , round(t[k+1], 3), ')=', y[k+1])
    plt.plot(t, y)
    plt.show()
        
   

def euler_mejorado(t0, y0, h, n):
    t=np.zeros(n+1)
    y=np.zeros(n+1)
    t[0]=t0
    y[0]=y0
    print('y(' , t, ')=', y)
    for k in range(n):
        y0=y[k]+h*f(t[k],y[k])
        y[k+1]=y[k]+(h/2)*(f(t[k], y[k]) + f(t[k]+h, y0))
        t[k+1]=t[k]+h
        print('y(' , round(t[k+1], 3), ')=', y[k+1])
    plt.plot(t, y)
    plt.show()    


def RK4(t0, y0, h, n):
    t=np.zeros(n+1)
    y=np.zeros(n+1)
    t[0]=t0
    y[0]=y0
    print('y(' , t, ')=', y)
    for k in range(n):
        k1=f(t[k], y[k])
        k2=f(t[k]+h/2, y[k]+(h/2)*k1)
        k3=f(t[k]+h/2, y[k]+(h/2)*k2)
        k4=f(t[k]+h, y[k]+h*k3)
        y[k+1]=y[k]+(h/6)*(k1+2*k2+2*k3+k4)
        t[k+1]=t[k]+h
        print('y(' , round(t[k+1],3), ')=', y[k+1])
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('xi')
    plt.show()


if __name__=='__main__':
    # t0 es el valor donde se evalúa el PVI
    # y0 es el valor al que es igual el PVI
    # h es el número de paso que se debe dar
    # n es hasta el número de veces que se debe hacer
    RK4(0, 4.329, 0.001, 10)   
    