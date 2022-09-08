
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2

def run():
    resolución=100
    x=np.linspace(-10, 10, num=resolución)
    y=f(x)
    fig, ax = plt.subplots()
    plt.xlim=(-25,25)
    plt.ylim=(-25,25)
    ax.plot(x,y)
    ax.axhline(y=0, color='r')
    ax.axvline(x=0, color='r')
    plt.show()

if __name__=='__main__':

   run()    

#Para funciones trigonométricas se hace uso de numpy, ej: np.cos(x)