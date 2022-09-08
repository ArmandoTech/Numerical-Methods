import numpy as np


def calcular_r():
    A = np.array([
    [72, 0, 0, 9, 0, 0],
    [0,	2.88, 0, 0, 0, -4.5],
    [0, 0,	18, 9, 0, 0],
    [0, 0, 9, 12, 0, 0],
    [0, 0, 0, 0, 33, 0],
    [0, -4.5, 0, 0, 0, 33]
    ])

    y_medido=np.array(
    [[2],
    [0.5],
    [1],
    [0],
    [1.2],
    [5]
    ])


    Aprima = np.transpose(A)
    A_por_Aprima=np.dot(Aprima, A)
    A_por_Aprima_inversa=np.linalg.inv(A_por_Aprima)
    A_por_Aprima_inversa_por_APrima=np.dot(A_por_Aprima_inversa, Aprima)
    coeficientes=np.dot(A_por_Aprima_inversa_por_APrima, y_medido)
    print(f'coeficientes:', '\n', coeficientes)

if __name__ == '__main__':
    calcular_r()
    