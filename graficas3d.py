
from matplotlib import cm  #Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return np.sin(x) + 2*np.cos(y)

if __name__=='__main__':
    resolucion=100
    x = np.linspace(-4, 4, num=resolucion)
    y = np.linspace(-4, 4, num=resolucion)
    x, y = np.meshgrid(x,y)
    z=f(x,y)

    fig, ax=plt.subplots(subplot_kw={"projection":"3d"})
    surf = ax.plot_surface(x,y,z, cmap=cm.cool)
    fig.colorbar(surf)
    plt.show()