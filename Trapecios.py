import numpy as np


x=np.array([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132])
fx=np.array([6.2, 6, 5.9, 5.9, 6.2, 6.4, 6.5, 6.8, 6.9, 7.1, 7.3, 6.9])
tamañox=len(x)
h=(x[tamañox-1]- x[0])/(tamañox-1)
tamañofx=len(fx)
y=sum(fx)
sumatoria=y-fx[0]-fx[tamañofx-1] #SUMATORIA ENTRE EL 2DO FX Y EL PENULTIMO FX
q=(fx[0]+fx[tamañofx-1])
respuesta= h/2 * (q + 2*(sumatoria))
print("La respuesta es: ", respuesta)