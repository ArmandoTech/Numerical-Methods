import numpy as np

A = np.array([
[-1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, -1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, -1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, -1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, -1, 0, 0, 5, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, -0.84],
[-0.7, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[-0.55, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, -0.2, 1, 0, 0],
[0, -0.85, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, -3.2, 1, 1, 0, 0, 0, 0 ]
])

B = np.array([
[0],
[0],
[0],
[0],
[100],
[0],
[0],
[0],
[0],
[0],
[0],
[0]
])


Aprima = np.transpose(A)
A_por_Aprima=np.dot(Aprima, A)
A_por_Aprima_inversa=np.linalg.inv(A_por_Aprima)
A_por_Aprima_inversa_por_APrima=np.dot(A_por_Aprima_inversa, Aprima)
Respuesta=np.dot(A_por_Aprima_inversa_por_APrima, B)

print(Respuesta)